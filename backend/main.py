from http import client
from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient('localhost', 27017)
db = client["hiphopdb"]
artists_collection = db["artists"]
records_collection = db["labels"]
hiphop_collection = db["hiphop"]

@app.get("/api/artists")
async def getArtists():
    artists = []
    for doc in artists_collection.find():
        artists.append(doc)
    return artists


@app.get("/api/records")
async def getRecords():
    records = []
    for record in records_collection.find():
        records.append(record)
    return records

@app.get("/api/hiphop")
async def getHipHop():
    hiphop = []
    for h in hiphop_collection.find():
        hiphop.append(h)
    return hiphop
