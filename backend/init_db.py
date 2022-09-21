from http import client
from SPARQLWrapper import SPARQLWrapper, JSON
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["hiphopdb"]
collection = db["hiphopcol"]
 
artists = ["Eminem", "Akon"]
id = 1

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
                dbo:birthPlace ?birthPlace .
        }
        """ % (artist)
    )
    sparql.setReturnFormat(JSON)
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        if(r["abstract"]["xml:lang"] == "en"):
            dict = {
                "_id": id,
                "name": artist,
                "birthDate": r["birthDate"]["value"],
                "birthPlace": r["birthPlace"]["value"],
                "abstract": r["abstract"]["value"],
            }
            id += 1
            # collection.insert_one(dict)
            print(dict)