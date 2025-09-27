from pymongo import MongoClient
from datetime import datetime
from flight_data import get_flights

def ingest(source,destination,date):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_ai"]
    collection = db["flight_details"]
    flights=get_flights(src_city=source,dest_city=destination,start_date=date)
    collection.insert_many(flights)

def read_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_ai"]
    flights=db.flight_details.find({ "arrival_city":"BANGALORE","departure_city": "KOCHI" ,"departure_date":"2025-11-20"})
    for flight in flights:
        print(flight)


if __name__ == "__main__":
    print("injest")
    ingest(source='kochi',destination='bangalore',date='2025-09-29')
    #read_data()
       




