from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI
from .flight_controller import read_flight_data
from .booking_controller import create_booking

app = FastAPI()

class PaymentDetails(BaseModel):
    number: str
    name: str
    expiry_date: str
    cvv: str

@app.get("/flights")
def get_flights(src_city: str,
                dest_city: str,
                start_date: str,
                ):
    return read_flight_data(src_city, dest_city, start_date,)


@app.post("/book_flight")
def book_flight(flight_id: str,
                name: str,
                adults: int,
                email: str,
                payment_details: PaymentDetails
                ):
    return create_booking(flight_id,
                name,
                adults,
                email,
                payment_details)

@app.get("/change_booking")
def change_booking(flight_number: str,
                start_date: str,
                adults):
    return {"status": "success", "booking_id": "12345"}

