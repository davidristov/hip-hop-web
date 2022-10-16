from SPARQLWrapper import SPARQLWrapper, JSON
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["hiphopdb"]
artists_collection = db["artists"]
records_collection = db["labels"]
hiphop_collection = db["hiphop"]
 
artists = ["Eminem", "Akon", "Snoop_Dogg", "Dr._Dre", "Kendrick_Lamar"]
records = ["Def_Jam_Recordings", "Aftermath_Entertainment", "Cash_Money_Records"]
id = 1 # used for primary key, tmp solution

artists = ["Eminem", "Akon", "Snoop_Dogg", "Dr._Dre", "Kendrick_Lamar"]

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
                dbo:thumbnail ?thumbnail ;
                dbo:birthName ?birthName .
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
            "thumbnail": r["thumbnail"]["value"],
            "birthName": r["birthName"]["value"]
            }
        id += 1
        artists_collection.insert_one(dict)

id = 1

for record in records:
    sparql.setQuery("""
        PREFIX dbp: <http://dbpedia.org/resource/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT *
        WHERE {
            dbr:%s dbo:abstract ?abstract ;
                   dbp:location ?location ;
                   dbp:country ?country ;
                   dbp:founder ?founder .
            FILTER(lang(?abstract)="en")     
        }
        """ % (record)
    )
    sparql.setReturnFormat(JSON)
    ret = sparql.queryAndConvert()

    location = []
    abstract = []
    country = []
    founders = []

    for r in ret["results"]["bindings"]:
        if(r["location"]["value"] not in location):
            location.append(r["location"]["value"])

        if r["abstract"]["value"] not in abstract: abstract.append(r["abstract"]["value"])
        if(r["founder"]["value"] not in founders):
            founders.append(r["founder"]["value"])

        c = r["country"]["value"].split("/")[-1]
        if (c not in country):
            country.append(c)

    dict = {
        "_id": id,
        "name": record,
        "abstract": abstract,
        "location": location,
        "country": country,
        "founders": founders
        # "foundingYear": r["foundingYear"]["value"],
    }
    records_collection.insert_one(dict)
    id += 1
    
sparql.setQuery("""
        PREFIX dbp: <http://dbpedia.org/resource/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT *
        WHERE {
            dbr:Hip_hop_music dbo:abstract ?abstract ;
                   dbo:instrument ?instrument ;
                   dbo:thumbnail ?thumbnail ;
                   dbp:culturalOrigins ?culturalOrigins .
            FILTER(lang(?abstract)="en")     
        }
        """
    )

sparql.setReturnFormat(JSON)
ret = sparql.queryAndConvert()
id = 1

instruments = []
abstract = []
thumbnail = []

for r in ret["results"]["bindings"]:
    if r["instrument"]["value"] not in instruments: instruments.append(r["instrument"]["value"])
    if r["abstract"]["value"] not in abstract: abstract.append(r["abstract"]["value"])
    if r["thumbnail"]["value"] not in thumbnail: thumbnail.append(r["thumbnail"]["value"])

dict = {
    "_id": id,
    "abstract": abstract,
    "thumbnail": thumbnail,
    "instruments": instruments,
    "culturalOrigins": r["culturalOrigins"]["value"]
}

hiphop_collection.insert_one(dict)