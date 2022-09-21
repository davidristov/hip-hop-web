from http import client
from SPARQLWrapper import SPARQLWrapper, JSON
from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()

client = MongoClient('localhost', 27017)
db = client["hiphopdb"]
collection = db["hiphopcol"]

@app.get("/api/artist/{name}")
async def getArtist(name: str):
    return collection.find_one({"name": name})