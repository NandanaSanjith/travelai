from .db_client import get_db_client

def read_flight_data(departure_city,arrival_city,start_date):
    db = get_db_client()
    flights=db.flight_details.find({ "arrival_city":arrival_city.upper(),
                                    "departure_city" :departure_city.upper() ,
                                    "departure_date":start_date})
    print(flights)
    return [_serialize_flight(f) for f in flights]

def _serialize_flight(flight):
    print(flight)
    flight["_id"] = str(flight["_id"])
    return flight