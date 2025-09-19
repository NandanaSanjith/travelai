from pymongo import MongoClient
from datetime import datetime

def ingest():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_ai"]
    collection = db["flight_details"]
    date_string= "2025-09-19"
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    collection.insert_one(
        {"flight_id":100,"source": "Kochi", "destination": "banglore",
         "date_time":date_obj,"available_seats":20,"seat_type":"economy"})
    print("completed")
    
if __name__ == "__main__":
    print("injest")
    ingest()
       




