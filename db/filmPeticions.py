from db import filmConnection
from bson.objectid import ObjectId
from datetime import datetime
import json

#SCHEMA
def film_schema(film)->dict:
    return {"id": str(film["_id"]),
            "title": film["title"],
            "director": film["director"],
            "year": film["year"],
            "genere": film["genre"],
            "rating": film["rating"],
            "country": film["country"],
            "created_at": film["created_at"],
            "update_at": film["update_at"]
    }
    
def films_schema(films) ->dict:
    return[film_schema(film) for film in films]

    
def getAllFilms():
    try:    
        conn = filmConnection.db()
        data = conn.films.find()
        films = [film_schema(film) for film in data]
        if films:
            result = {
                "status": 1,
                "data": films
            }
        else:
            result = {
                "status": -1,
                "message": "Cap pel·lícula trobada"
            }
        return result
    except Exception as e:
        return {
            "status": -1,
            "message": f'Error de connexió: {e}'
        }

def getFilmById(id):
    try:    
        conn = filmConnection.db()
        data = conn.films.find_one({"_id" : ObjectId(id)})
        if data:
            result = {
                "status": 1,
                "data": film_schema(data)
            }
        else:
            result = {
                "status": -1,
                "message": "Cap pel·lícula trobada"
            }
        return result
    except Exception as e:
        return {
            "status": -1,
            "message": f'Error de connexió: {e}'
        }

def createFilm(new_film_data):
    try:
        conn = filmConnection.db()
        now = datetime.now()
        data = {
            "title": new_film_data.title,
            "director": new_film_data.director,
            "year": new_film_data.year,
            "genre": new_film_data.genre,
            "rating": new_film_data.rating,
            "country": new_film_data.country,
            "created_at": now,
            "update_at": now
        }
        id = conn.films.insert_one(data).inserted_id
        
        response = {
            "status": 1,
            "data": {
                "id": str(id)
                }
        }
        
        return response;
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}

def updateFilm(id, updateFilm):
    try:
        conn = filmConnection.db()
        now = datetime.now()
        data={
            "title": updateFilm.title,
            "director": updateFilm.director,
            "year": updateFilm.year,
            "genre": updateFilm.genre,
            "rating": updateFilm.rating,
            "country": updateFilm.country,
            #EL CREATE NO L'HAIG DE TOCAR. 
            "update_at": now
        }  
        conn.films.update_one({"_id" : ObjectId(id)}, {"$set": data})
        response = {
                "status": 1,
                "data": {
                    "id": id
                }
            }
        return response
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    
def deleteFilm(id):
    try:
        conn = filmConnection.db()
        result = conn.films.delete_one({"_id": ObjectId(id)})
        
        if result.deleted_count > 0:
            return {"status": 1, "message": "La pel·lícula s'ha esborrat correctament"}
        else:
            return {"status": -1, "message": "La pel·lícula no s'ha trobat a la BBDD"}
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    
def getFilmsByGenre(genre):
    try:
        conn = filmConnection.db()
        data = conn.films.find({"genre": genre})
        films = [film_schema(film) for film in data]
        if films:
            result = {
                "status": 1,
                "data": films
            }
        else:
            result = {
                "status": -1,
                "message": f"Cap pel·lícula trobada pel gènere: {genre}"
            }
        return result
    except Exception as e:
        return {
            "status": -1,
            "message": f'Error de connexió: {e}'
    }

def getFilmsByOrder(field, order):
    try:    
        conn = filmConnection.db()
        data = conn.films.find().sort(field, order)
        result = films_schema(data)
        response = {
            "status": 1,
            "data": result
        }
        return response
    except Exception as e:
        return {
            "status": -1,
            "message": f'Error de connexió: {e}'
    }

def getFilmsByLimit(limit):
    try:
        conn = filmConnection.db();
        data = conn.films.find().limit(limit)
        result = films_schema(data)
        return result
    except Exception as e:
        return {
            "status": -1,
            "message": f'Error de connexió: {e}'
    }
