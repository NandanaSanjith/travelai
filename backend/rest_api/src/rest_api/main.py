from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI
from .flight_controller import read_flight_data,get_airports,get_flight_details
from .booking_controller import create_booking,generate_booking_id,insert_booking
from .payment_controller import create_order,insert_payment_record
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
    payment_session=create_order(amount_in_rupee)
    insert_booking(booking_id,booking_details.name,booking_details.email,
                   payment_session["payment_id"],booking_details.adults,booking_details.id)
    insert_payment_record(payment_session["payment_id"],booking_id,"pending",payment_session["url"])
    return {"booking_id": booking_id,"payment_session": payment_session}



@app.get("/airports")
def airports():
    return get_airports()


