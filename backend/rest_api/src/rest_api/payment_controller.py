import stripe
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")


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
        return {"url": session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
