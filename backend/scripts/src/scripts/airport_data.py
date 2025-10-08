
import pandas as pd

from pymongo import MongoClient

def injest_airport_data():
 url = "https://ourairports.com/data/airports.csv"
 df = pd.read_csv(url)

 indian_airports = df[(df["iso_country"] == "IN") & (df["type"]== "large_airport")][["name", "municipality", "iata_code", "type"]]
 records = indian_airports.to_dict(orient="records")
 client = MongoClient("mongodb://localhost:27017/")  # or your connection URI
 db = client["travel_ai"]
 collection = db["airports"]
 collection.delete_many({})
 result = collection.insert_many(records)
 print("done.")

if __name__ == "__main__":
   injest_airport_data()