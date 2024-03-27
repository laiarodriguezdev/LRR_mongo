from db import filmConnection
from bson.objectid import ObjectId
from datetime import datetime
import json

#Schema que ara  per poder operar amb l'objecte 
def film_schema(film)->dict:
    return {"id": str(film["_id"]),
            "title": film["title"],
            "director": film["director"],
            "year": film["year"],
            "genere": film["genre"],
            "rating": film["rating"],
            "country": film["country"],
    }
    
def films_schema(films) ->dict:
    return[film_schema(film) for film in films]

    
def getAllFilms():
    try:    
        conn = filmConnection.db()
        data = conn.films.find()
        result = [film_schema(film) for film in data]
        return result
    except Exception as e:
        return f'Error connexió: {e}'

def getFilmById(id):
    try:    
        conn = filmConnection.db()
        data = conn.films.find_one({"_id" : ObjectId(id)})
        result = film_schema(data)
        return result
    except Exception as e:
        return f'Error connexió: {e}'

def getFilmsByGen(genre):
    try:
        conn = filmConnection.db()
        data = conn.films.find()
        data=conn.films.find({"genre": genre})
        result = films_schema(data)
        return result
    except Exception as e:
        return f'Error conexió {e}'
    