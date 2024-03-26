from db import film
from bson.objectid import ObjectId
from datetime import datetime
import json

#Schema que ara  per poder operar amb l'objecte 
def film_schema(film)->dict:
    return {"id": str(film["_id"]),
            "title": film["title"],
            "director": film["director"],
            "year": film["year"],
            "genere": film["genere"],
            "rating": film["rating"],
            "country": film["country"],
    }
    
def films_schema(films) ->dict:
    return[film_schema(film) for film in films]


    
def consulta():
    try:    
        conn = film.db()
        data = conn.db.find()
        result = data
        return result
    except Exception as e:
        return f'Error connexió: {e}'
    