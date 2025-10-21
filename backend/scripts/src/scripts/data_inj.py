from pymongo import MongoClient
from datetime import datetime
from flight_data import get_flights
client = MongoClient("mongodb://localhost:27017/")

def ingest(source,src_iata,destination,dest_iata,date):
    db = client["travel_ai"]
    collection = db["flight_details"]
    flights=get_flights(src_city=source,src_city_iata=src_iata,dest_city=destination,dest_city_iata=dest_iata, start_date=date)
    collection.insert_many(flights)

def read_data():
    db = client["travel_ai"]
    flights=db.flight_details.find({ "arrival_city":"BANGALORE","departure_city": "KOCHI" ,"departure_date":"2025-11-20"})
    for flight in flights:
        print(flight)

def get_airport():
    db = client["travel_ai"]
    collection = db["airports"]
    airports = list(collection.find({}, {"_id": 0}))
    return airports

def clear_flight_details():
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
                ingest(source=src_airport["municipality"],
                       src_iata=src_airport["iata_code"],
                       destination= dest_airport["municipality"],
                       dest_iata=dest_airport["iata_code"],
                       date='2025-10-21')
                
    #read_data()
       




