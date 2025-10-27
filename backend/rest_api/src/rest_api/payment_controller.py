import stripe
import os
from dotenv import load_dotenv
from .db_client import get_db_client
from fastapi import HTTPException

load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")



def create_order(total_amount_rupee):
    try:
        total_amount_paise=total_amount_rupee*100
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
            success_url="http://localhost:5173/success",
            cancel_url="http://localhost:5173/cancel",
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