from typing import Union, List, Dict, Any
from datetime import datetime, timedelta
import random

def get_flights(src_city: str,
                dest_city: str,
                start_date: str,
                ) -> List[Dict[str, Any]]:
    """
    Generate sample flight data between two cities for a given date range.

    Args:
        src_city: Source city code or name (e.g., "COK" for Kochi)
        dest_city: Destination city code or name (e.g., "BLR" for Bangalore)
        start_date: Start date in YYYY-MM-DD format
        return_date: Return date in YYYY-MM-DD format

    Returns:
        List of dictionaries containing flight information
    """
    flights = []

    # Generate flights for each day in the next 30 days
    base_date = datetime.strptime(start_date, "%Y-%m-%d")
    for day in range(30):
        current_date = base_date + timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")

        # Generate 3-5 flights per day
        for _ in range(random.randint(3, 5)):
            # Generate random departure time between 6 AM and 10 PM
            departure_hour = random.randint(6, 22)
            departure_minute = random.choice([0, 15, 30, 45])
            departure_time = f"{departure_hour:02d}:{departure_minute:02d}"

            # Flight duration between 1 to 3 hours
            duration_hours = random.randint(1, 3)
            duration_minutes = random.choice([0, 15, 30, 45])

            # Calculate arrival time
            arrival_hour = (departure_hour + duration_hours) % 24
            arrival_minute = (departure_minute + duration_minutes)
            if arrival_minute >= 60:
                arrival_hour += 1
                arrival_minute -= 60
            arrival_time = f"{arrival_hour:02d}:{arrival_minute:02d}"

            # Generate random airline and flight number
            airlines = ["IndiGo", "Air India", "Vistara", "AirAsia", "SpiceJet"]
            airline = random.choice(airlines)
            flight_number = f"{airline[:2].upper()}{random.randint(100, 999)}"

            # Generate random price
            base_price = random.randint(2000, 10000)
            price = base_price
            seat_types = ["Business", "Economy", "Premium"]
            random_seat = random.choice(seat_types)

            flight = {
                "airline": airline,
                "flight_id": flight_number,
                "departure_city": src_city.upper(),
                "arrival_city": dest_city.upper(),
                "departure_date": date_str,
                "departure_time": departure_time,
                "arrival_date": date_str,
                "arrival_time": arrival_time,
                "duration": f"{duration_hours}h {duration_minutes}m",
                "price": price,
                "stops": random.choice(["Non-stop", "1 stop", "2 stops"]),
                "available_seats": random.randint(5, 50),
                "seat_type":random_seat
            
            }
            flights.append(flight)

    return flights