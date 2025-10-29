import os
import time
from dotenv import load_dotenv
from fastapi import HTTPException 
import requests
from jinja2 import Environment, FileSystemLoader

load_dotenv()
ZOHO_API_KEY= os.getenv("ZOHO_API_KEY")

env = Environment(loader=FileSystemLoader('templates'))

def send_email(to_email, to_name, subject, message):
    url = "https://api.zeptomail.com/v1.1/email"

    payload = {
        "from": {
            "address": "noreply@stoczai.com",
            "name": "Wanderwise"
        },
        "to": [
            {
                "email_address": {
                    "address": to_email,
                    "name": to_name
                }
            }
        ],
        "subject": subject,
        "htmlbody": message
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": ZOHO_API_KEY
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code in (200, 201):
        print(f"✅ Successfully sent email to: {to_email}")
        return {"status": "success", "message": "Email sent successfully"}
    else:
        error_msg = response.json().get("error", {}).get("message", "Failed to send email")
        raise HTTPException(status_code=response.status_code, detail=error_msg)
    
    
def _get_airport_name(airports, airport_code):
    for a in airports:
        if a['iata_code'].strip().lower() == airport_code.strip().lower():
            return a['name'].upper()
    return airport_code.upper()


def send_confirmation_email(booking_details,flight_details):
    if not booking_details or not flight_details:
        raise HTTPException(status_code=404, detail="Invalid input")
    template = env.get_template('booking_confirmation.html')
    template_variables={
        'name':booking_details["name"],
        'email':booking_details["email"],
        'booking_id':booking_details["booking_id"],
        'total_passengers':booking_details["total_passengers"],

        'flight_number':flight_details["flight_id"].upper(),
        'airline_name':flight_details["airline"].upper(),
        'total_amount':flight_details["price"]*booking_details["total_passengers"]

        # Departure details
        'departure_city': flight_details['departure_city'].upper(),
        'departure_city_iata': flight_details['departure_city_iata'].upper(),
        'departure_airport': _get_airport_name(airports, flight_details['departure_city_iata']),
        'departure_time': flight_details['departure_time'].upper(),
        'departure_date': flight_details['departure_date'].upper(),

        # Arrival details
        'arrival_city': flight_details['arrival_city'].upper(),
        'arrival_city_iata': flight_details['arrival_city_iata'].upper(),
        'arrival_airport': _get_airport_name(airports, flight_details['arrival_city_iata']),
        'arrival_time': flight_details['arrival_time'].upper(),
        'arrival_date': flight_details['arrival_date'].upper()


    }

