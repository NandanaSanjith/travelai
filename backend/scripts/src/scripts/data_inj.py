from pymongo import MongoClient
from datetime import datetime
from flight_data import get_flights

def ingest(source,destination,date):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_ai"]
    collection = db["flight_details"]
    flights=get_flights(src_city=source,dest_city=destination,start_date=date)
    collection.insert_many(flights)

    
if __name__ == "__main__":
    print("injest")
    ingest(source='kochi',destination='banglore',date='2025-10-29')

       




