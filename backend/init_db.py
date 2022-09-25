# from http import client
import re
from SPARQLWrapper import SPARQLWrapper, JSON
from pymongo import MongoClient
import urllib.request


client = MongoClient('localhost', 27017)
db = client["hiphopdb"]
artists_collection = db["artists"]
records_collection = db["labels"]
 
artists = ["Eminem", "Akon", "50_Cent"]
records = ["Aftermath_Entertainment", "Death_Row_Records"]
id = 1 # used for primary key, tmp solution

for artist in artists:
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX dbp: <http://dbpedia.org/resource/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT *
        WHERE {
            dbr:%s dbo:abstract ?abstract ;
                dbo:birthDate ?birthDate ;
                dbo:birthPlace ?birthPlace ;
                dbo:thumbnail ?thumbnail .
            FILTER(lang(?abstract)="en")
        }
        """ % (artist)
    )
    sparql.setReturnFormat(JSON)
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        dict = {
            "_id": id,
            "name": artist,
            "birthDate": r["birthDate"]["value"],
            "birthPlace": r["birthPlace"]["value"],
            "abstract": r["abstract"]["value"],
            "thumbnail": r["thumbnail"]["value"]
            }
            # image = r["thumbnail"]["value"]
            # print(image)
            # urllib.request.urlretrieve(image, "./frontend/" + dict["name"] + ".jpg")
        id += 1
        artists_collection.insert_one(dict)

id = 0

for record in records:
    sparql.setQuery("""
        PREFIX dbp: <http://dbpedia.org/resource/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT *
        WHERE {
            dbr:%s dbo:abstract ?abstract ;
                   dbo:location ?location ;
                   dbp:country ?country .
            FILTER(lang(?abstract)="en")     
        }
        """ % (record)
    )
    sparql.setReturnFormat(JSON)
    ret = sparql.queryAndConvert()

    location = []
    abstract = []
    country = []
    for r in ret["results"]["bindings"]:
        location.append(r["location"]["value"])
        abstract.append(r["abstract"]["value"])
        country.append(r["country"]["value"])

    dict = {
        "_id": id,
        "name": record,
        "abstract": abstract,
        "location": location,
        "country": country
    }
    records_collection.insert_one(dict)
    id += 1
    