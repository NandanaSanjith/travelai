from typing import Any, List, Dict
import httpx
from mcp.server.fastmcp import FastMCP
import requests

# Initialize FastMCP server
mcp = FastMCP("Flight Booking System")

@mcp.tool()
def get_flights(src_city_iata_code: str,
                dest_city_iata_code: str,
                start_date: str,
                adults: int ,) -> List[Any]:
    """Get a list of available flights
        Args:
            src_city_iata_code (str, required): Source city iata code, Eg: Bangalore airport iata code is BLR
            dest_city_iata_code (str,required): Destination city iata code, Eg: Kochi airport iata code is COK
            start_date (str, required):  Start date of the journey
            adults (int, required): total number of passengers ask the customer to enter this number.
        Returns:
            list: List of available flights
    """
    params = {
        "src_city": src_city_iata_code,
        "dest_city": dest_city_iata_code,
        "start_date": start_date,
        "adults": adults
    }
    response = requests.get("http://localhost:8000/flights", params=params)
    response.raise_for_status()
    return response.json()

@mcp.tool()
def start_booking_flight(id: str,
                name: str,
                adults: int,
                email: str,
                passenger_details: List[Dict[str, str]]
                )  -> Dict[str, Any]:
    """ This method will start a booking of flight and block the seats till the payment is done.
        Args:
            id (str, required): _id received in get_flights method response
            name (str, required): Name of the person who is booking
            email (str, required): Email of the person who is booking
            adults (int, required): Number of adults, ask the customer the number of passengers travelling and assign to adults.
            passenger_details (List[Dict], required): List of passenger details. Must contain exactly 'adults' number of entries.
                Each entry must have:
                - name (str): Full name of the passenger
                - identification_type (str): Type of ID (e.g., "Passport", "Aadhar", "Driver's License")
                - identification_number (str): ID number
                
                Example: [
                    {"name": "John Doe", "identification_type": "Passport", "identification_number": "A1234567"},
                    {"name": "Jane Doe", "identification_type": "Aadhar", "identification_number": "1234-5678-9012"}
                ]
        
        Returns:
        dict
            booking_id: An id indicating the booking
            payment_session: A dictionary containing url and a payment session id.
            Customer has to complete the payment using the url.
            If the payment is not complete in 30 minutes the booking will be cancelled.
            An email will be sent with the booking confirmation after the payment is done.
    """
    
    # Validate passenger_details count matches adults
    if len(passenger_details) != adults:
        raise ValueError(f"passenger_details must contain exactly {adults} entries to match the number of adults")
    
    # Validate each passenger detail has required fields
    required_fields = {"name", "identification_type", "identification_number"}
    for i, passenger in enumerate(passenger_details):
        missing_fields = required_fields - set(passenger.keys())
        if missing_fields:
            raise ValueError(f"Passenger {i+1} is missing required fields: {missing_fields}")

    params = {
        "id": id,
        "name": name,
        "adults": adults,
        "email": email,
        "passenger_details": passenger_details
    }
    response = requests.post("http://localhost:8000/start_booking", json=params)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio') 