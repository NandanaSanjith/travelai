from typing import Union
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
import stripe
from .flight_controller import (read_flight_data,
                                get_airports,
                                get_flight_details,
                                update_available_seats)
from .booking_controller import (create_booking,
                                 generate_booking_id,
                                 insert_booking,
                                 update_booking_status)
from .payment_controller import (create_order,
                                 insert_payment_record,
                                 update_payment_status)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PaymentDetails(BaseModel):
    number: str
    name: str
    expiry_date: str
    cvv: str

class BookingDetails(BaseModel):
    flight_id: str
    name: str
    adults: int
    email: str
    payment_details:PaymentDetails


class StartBookingDetails(BaseModel):
    id: str
    name: str
    adults: int
    email: str

@app.get("/flights")
def get_flights(src_city: str,
                dest_city: str,
                start_date: str,
                ):
    return read_flight_data(src_city, dest_city, start_date,)


@app.post("/book_flight")
def book_flight(booking_details:BookingDetails):
    return create_booking(booking_details.flight_id,
                booking_details.name,
                booking_details.adults,
                booking_details.email,
                booking_details.payment_details)


@app.get("/change_booking")
def change_booking(flight_number: str,
                start_date: str,
                adults):
    return {"status": "success", "booking_id": "123456"}

@app.post("/start_booking")
def start_booking(booking_details:StartBookingDetails):
    booking_id=generate_booking_id()
    flight_details=get_flight_details(booking_details.id)
    amount_in_rupee=flight_details["price"]*booking_details.adults
    payment_session=create_order(amount_in_rupee,booking_id)
    insert_booking(booking_id,booking_details.name,booking_details.email,
                   payment_session["payment_id"],booking_details.adults,booking_details.id)
    insert_payment_record(payment_session["payment_id"],booking_id,"pending",payment_session["url"])
    available_seats=flight_details["available_seats"]-booking_details.adults
    update_available_seats(booking_details.id,available_seats)
    return {"booking_id": booking_id,"payment_session": payment_session}




@app.get("/airports")
def airports():
    return get_airports()

@app.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    session = event['data']['object']
    session_id=session["id"]
    booking_id=session.get("metadata",{}).get("booking_id")
    print(session_id,booking_id)
    # ✅ Handle events
    if event['type'] == 'checkout.session.completed':
        print("💰 Payment was successful!")
        update_booking_status(booking_id,"success")
        update_payment_status(session_id,"success")

    elif (event['type'] == 'payment_intent.payment_failed' or
        event['type']=='checkout.session.expired'):
        print("❌ Payment failed!")
        update_booking_status(booking_id,"failed")
        update_payment_status(session_id,"failed")
    return {"status": "success"}