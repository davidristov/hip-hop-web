# hip-hop-web

Simple web project with FastAPI, MongoDB, ReactJS. Uses SPARQL to query dbpedia and stores data into MongoDB.

## Run

Start MongoDB:
`docker run -d -p 27017:27017 mongo:latest`

Run queries and populate the DB:
`python3 init_db.py`

Start backend:
`uvicorn main:app --reload`

Start frontend:
`npm start`

## TO-DO

`docker-compose.yaml` (maybe)
...