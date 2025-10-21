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
                adults: int = 1,) -> List[Any]:
    """Get a list of available flights
        Args:
            src_city_iata_code (str, required): Source city iata code, Eg: Bangalore airport iata code is BLR
            dest_city_iata_code (str,required): Destination city iata code, Eg: Kochi airport iata code is COK
            start_date (str, required):  Start date of the journey
            adults (int, optional): Number of adults. Defaults to 1.
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
def book_flight(flight_id: str,
                name: str,
                adults: int,
                email: str,
                credit_card_number : str,
                credit_card_holder_name : str,
                expiry_date : str,
                cvv : str
                )  -> Dict[str, Any]:
    """Book a flight
        Args:
            flight_id (str, required): Flight number
            name (str, required):  Name of the person who is booking
            email (str, required):  email of the person who is booking
            adults (int, required): Number of adults. Defaults to 1.
            credit_card_number(str, required) : Creditcard number used for booking
            credit_card_holder_name(str, required) : person who owns the creditcard
            expiry_date(str, required) : expiry date of creditcard
            cvv(str,required): 3 digit number behind the credit card
    """

    params = {
        "flight_id": flight_id,
        "name": name,
        "adults": adults,
        "email" : email,
        "payment_details" : {
            "number": credit_card_number,
            "name": credit_card_holder_name,
            "expiry_date": expiry_date,
            "cvv": cvv
        }
    }
    response = requests.post("http://localhost:8000/book_flight", json=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio') 