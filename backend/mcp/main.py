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
def start_booking_flight(id: str,
                name: str,
                adults: int,
                email: str,
                )  -> Dict[str, Any]:
    """ This method will start a booking of flight and block the seats till the payment is done.
        Args:
            id (str, required): _id recieved in get_flights method response
            name (str, required):  Name of the person who is booking
            email (str, required):  email of the person who is booking
            adults (int, required): Number of adults. Defaults to 1.
        return:
        dict
            booking_id:an id indicating the booking
            payment_session:a dictionary containing url and a payment session id.
            Customer has to complete the payment using the url.
            If the payment is not complete in 30 minutes the booking will be cancelled.
            An email will be sent with the booking confirmation after the payment is done.
    """

    params = {
        "id": id,
        "name": name,
        "adults": adults,
        "email" : email,
    }
    response = requests.post("http://localhost:8000/start_booking", json=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio') 