from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI
from .flight_controller import read_flight_data,get_airports
from .booking_controller import create_booking
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

@app.get("/airports")
def airports():
    return get_airports()


