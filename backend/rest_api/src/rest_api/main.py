from typing import Union

from fastapi import FastAPI
from .flight_fake_data import get_fake_flights

app = FastAPI()

@app.get("/flights")
def get_flights(src_city: str,
                dest_city: str,
                start_date: str,
                adults: int = 1,):
    return get_fake_flights(src_city, dest_city, start_date, adults)

@app.get("/book_flight")
def book_flight(flight_number: str,
                start_date: str,
                adults):
    return {"status": "success", "booking_id": "12345"}

@app.get("/change_booking")
def change_booking(flight_number: str,
                start_date: str,
                adults):
    return {"status": "success", "booking_id": "12345"}