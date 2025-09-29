from pymongo import MongoClient

def get_db_client():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_ai"]
    return db