from typing import Union, Optional, List
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
                                 update_booking_status,
                                 get_booking_details,
                                 get_booking_details_json)
from .payment_controller import (create_order,
                                 insert_payment_record,
                                 update_payment_status,
                                 get_payment_json)
from .email_controller import (send_confirmation_email)
from .chat_controller import ClaudeClient
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
claude_chat_client=None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global claude_chat_client
    # Startup
    claude_chat_client = ClaudeClient()
    await claude_chat_client.initialize()  # Make sure this is awaited
    yield
    # Shutdown
    if claude_chat_client:
        await claude_chat_client.close()  # Add a close method to clean up resources
        print("Claude client shut down")

app = FastAPI(lifespan=lifespan)
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

class ChatMessage(BaseModel):
    message: str
    reset_conversation: bool = False

class PassengerDetails(BaseModel):
    name: str
    identification_type: str
    identification_number: str


class StartBookingDetails(BaseModel):
    id: str
    name: str
    adults: int
    email: str
    passenger_details: Optional[List[PassengerDetails]] = []

@app.get("/flights")
def get_flights(src_city: str,
                dest_city: str,
                start_date: str,
                ):
    return read_flight_data(src_city, dest_city, start_date,)


@app.get("/booking")
def booking(booking_id: str):
    booking_details=get_booking_details_json(booking_id)
    flight_details=get_flight_details(booking_details["flight_id"])
    payment_details=get_payment_json(booking_details["payment_id"])
    return {"booking_details": booking_details, "flight_details": flight_details, "payment_details": payment_details}  

@app.post("/start_booking")
def start_booking(booking_details:StartBookingDetails):
    booking_id=generate_booking_id()
    flight_details=get_flight_details(booking_details.id)
    amount_in_rupee=flight_details["price"]*booking_details.adults
    payment_session=create_order(amount_in_rupee,booking_id)
    print(payment_session["url"])
    passenger_details_list = [p.dict() for p in booking_details.passenger_details]
    insert_booking(booking_id,
                   booking_details.name,
                   booking_details.email,
                   payment_session["payment_id"],
                   booking_details.adults,
                   booking_details.id,
                   passenger_details_list)
    insert_payment_record(payment_session["payment_id"],
                          booking_id,"pending",
                          payment_session["url"])
    available_seats=flight_details["available_seats"]-booking_details.adults
    update_available_seats(booking_details.id,available_seats)
    return {"booking_id": booking_id,"payment_session": payment_session}




@app.get("/airports")
def airports():
    return get_airports()

@app.get("/send_testmail")
def send_test():
    print ("sent test")
    booking_details=get_booking_details("LIFUYCYZ")
    flight_details=get_flight_details(booking_details['flight_id'])
    return send_confirmation_email(booking_details,flight_details)

@app.post("/chat")
async def chat(chat_message: ChatMessage):
    return await claude_chat_client.send_chat_message(chat_message.message,
                                                      chat_message.reset_conversation)



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
        booking_details=get_booking_details(booking_id)
        flight_details=get_flight_details(booking_details["flight_id"])
        update_booking_status(booking_id,"success")
        update_payment_status(session_id,"success")
        send_confirmation_email(booking_details,flight_details)
        
    elif (event['type'] == 'payment_intent.payment_failed' or
        event['type']=='checkout.session.expired'):
        print("❌ Payment failed!")
        update_booking_status(booking_id,"failed")
        update_payment_status(session_id,"failed")
    return {"status": "success"}