from typing import Union

from fastapi import FastAPI
from .flight_controller import read_flight_data
app = FastAPI()

@app.get("/flights")
def get_flights(src_city: str,
                dest_city: str,
                start_date: str,
                ):
    return read_flight_data(src_city, dest_city, start_date,)


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
