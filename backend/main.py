from http import client
from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()

client = MongoClient('localhost', 27017)
db = client["hiphopdb"]
artists_collection = db["artists"]
records_collection = db["labels"]

@app.get("/api/artist/{name}")
async def getArtistByName(name: str):
    return artists_collection.find_one({"name": name})


@app.get("/api/records/{name}")
async def getRecordByName(name: str):
    return records_collection.find_one({"name": name})