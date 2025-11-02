from .db_client import get_db_client
from .utils import is_valid_email,get_todays_date,convert_date_to_string
from bson import ObjectId
from fastapi import HTTPException
import random
import string




def is_payment_valid(payment_details):
    return True

def is_seat_available(total_seats):
    return True

def generate_booking_id(length=8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

def update_booking_status(id,booking_status):
    db=get_db_client()
    db.booking_details.update_one({"booking_id": id},
                                  {"$set": {"booking_status": booking_status}})

def get_booking_details(id):
    db=get_db_client()
    return db["booking_details"].find_one({"booking_id":id})

def get_booking_details_json(id):
    booking_details=get_booking_details(id)
    return _serialize_booking(booking_details)

def _serialize_booking(booking_details):
    booking_details["_id"] = str(booking_details["_id"])
    return booking_details

def create_booking(flight_id,
                name,
                adults,
                email,
                payment_details):
    if not is_valid_email(email):
        raise HTTPException(status_code=400, detail="Email is not valid")
    if adults < 0:
        raise HTTPException(status_code=400, detail="number of passengers not valid")
    if not is_payment_valid(payment_details):
        raise HTTPException(status_code=400, detail="Payment is not valid")
    if not is_seat_available(adults):
        raise HTTPException(status_code=400, detail="seats not available")
    booking_id=generate_booking_id()
    db=get_db_client()
    booking = { 
     "booking_id": booking_id,
     "name": name,
     "email": email,
     "booking_date": convert_date_to_string(get_todays_date()),
    "total_passengers": adults,
     "flight_id": flight_id
    }

    db["booking_details"].insert_one(booking)
    return {"status": "success", "booking_id": booking_id}

def insert_booking(booking_id,name,email,payment_id,adults,flight_id):
    db=get_db_client()
    booking = { 
     "booking_id": booking_id,
     "name": name,
     "email": email,
     "booking_date": convert_date_to_string(get_todays_date()),
    "total_passengers": adults,
     "flight_id": flight_id,
     "payment_id":payment_id,
     "booking_status":"pending"
    }
    db["booking_details"].insert_one(booking)

