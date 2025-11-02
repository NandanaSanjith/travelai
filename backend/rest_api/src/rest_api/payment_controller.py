import stripe
import os
import time
from dotenv import load_dotenv
from .db_client import get_db_client
from fastapi import HTTPException

load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")



def create_order(total_amount_rupee,booking_id):
    try:
        total_amount_paise=total_amount_rupee*100
        expire_time = int(time.time()) + (30 * 60)
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="payment",
            line_items=[{
                "price_data": {
                    "currency": "inr",
                    "product_data": {"name": "Wanderwise"},
                    "unit_amount": total_amount_paise,  # in paise
                },
                "quantity": 1,
            }],
            success_url=f"http://localhost:5173/success?booking_id={booking_id}",
            cancel_url=f"http://localhost:5173/cancel?booking_id={booking_id}",
            expires_at=expire_time,
            metadata={
                "booking_id": booking_id,
            }
        )
        return {"url": session.url,"payment_id":session.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def insert_payment_record(id,booking_id,payment_status,url):
    db=get_db_client()
    payment = { 
     "payment_id": id,
     "payment_status":payment_status,
     "booking_id":booking_id,
     "url":url
    }
    db["payment_details"].insert_one(payment)

def update_payment_status(id,payment_status):
    db=get_db_client()
    db.payment_details.update_one({"payment_id": id},
                                  {"$set": {"payment_status": payment_status}})
    
def _serialize_payment(payment):
    payment["_id"] = str(payment["_id"])
    return payment

def get_payment_json(id):
    db=get_db_client()
    payment = db.payment_details.find_one({"payment_id":id})
    return _serialize_payment(payment)
