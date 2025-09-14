from typing import Any, List, Dict
import httpx
from mcp.server.fastmcp import FastMCP
import requests

# Initialize FastMCP server
mcp = FastMCP("Flight Booking System")

@mcp.tool()
def get_flights(src_city: str,
                dest_city: str,
                start_date: str,
                adults: int = 1,) -> List[Any]:
    """Get a list of available flights
        Args:
            src_city (str, required): Source city, Eg: Kochi to Chennai
            dest_city (str,required): Destination city
            start_date (str, required):  Start date of the journey
            adults (int, optional): Number of adults. Defaults to 1.
        Returns:
            list: List of available flights
    """
    params = {
        "src_city": src_city,
        "dest_city": dest_city,
        "start_date": start_date,
        "adults": adults
    }
    response = requests.get("http://localhost:8000/flights", params=params)
    response.raise_for_status()
    return response.json()

@mcp.tool()
def book_flight(flight_number: str,
                start_date: str,
                adults)  -> Dict[str, Any]:
    """Book a flight
        Args:
            flight_number (str, required): Flight number
            start_date (str, required):  Start date of the journey
            adults (int, optional): Number of adults. Defaults to 1.
    """
    params = {
        "flight_number": flight_number,
        "start_date": start_date,
        "adults": adults
    }
    response = requests.get("http://localhost:8000/book_flight", params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio') 