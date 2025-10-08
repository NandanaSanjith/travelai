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

def get_airport():
    client = MongoClient("mongodb://localhost:27017/")  # or your connection URI
    db = client["travel_ai"]
    collection = db["airports"]
    airports = list(collection.find({}, {"_id": 0}))
    return airports

def clear_flight_details():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_ai"]
    collection = db["flight_details"]
    collection.delete_many({})

if __name__ == "__main__":
    print("starting injestion")
    clear_flight_details()
    airports= get_airport()
    for src_airport in airports:
        for dest_airport in airports:
            if src_airport["name"] != dest_airport["name"]:
                print("injesting data : %s,%s" %( src_airport["name"],dest_airport["name"]))
                ingest(source=src_airport["name"],destination= dest_airport["name"],date='2025-10-08')
                
    #read_data()
       




