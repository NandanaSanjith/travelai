from .db_client import get_db_client

def read_flight_data(departure_city,arrival_city,start_date):
    db = get_db_client()
    flights = db.flight_details.find({
     "arrival_city": { "$regex": arrival_city, "$options": "i" },
     "departure_city": { "$regex": departure_city, "$options": "i" },
     "departure_date": start_date
     }) 

    print(flights)
    return [_serialize_flight(f) for f in flights]

def _serialize_flight(flight):
    flight["_id"] = str(flight["_id"])
    return flight

def get_airports():
    db = get_db_client()
    airports = db.airports.find()
    return [_serialize_airport(a) for a in airports]

def _serialize_airport(airport):
    airport["_id"] = str(airport["_id"])
    return airport

