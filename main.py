from typing import Union
from fastapi import FastAPI
from Model.Film import Film
from db import filmPeticions

app = FastAPI(title="Laia Rodríguez Ramos - CRUD + Consultes avançades")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


#RETORNA TOTA LA LLISTA D'OBJECTES
@app.get("/films")
def getFilms():
    data = filmPeticions.getAllFilms()
    return data

#RETORNA LA PELI CORRESPONENT AL ID
@app.get("/films/{id}")
def getFilmById(id):
    data = filmPeticions.getFilmById(id)
    return data

#CREA UN NOU DOCUMENT
@app.post("/film/")
def createFilm(film: Film):
    data = filmPeticions.createFilm(film)
    return data

#ACTUALITZA UN NOU DOCUMENT/FILM. 
@app.put("/film/{id}")
def updateProduct(id, film:Film):
    data=filmPeticions.updateFilm(id, film)
    return data

#ESBORRA EL DOCUMENT/FILM. 
@app.delete("/film/{id}")
def deleteFilm(id):
    data=filmPeticions.deleteFilm(id)
    return data


#RETORNA LES PELIS DE ACTION, BIOGRAPHY, ETC. 
@app.get("/filmsGenre")
def getFilmsByGen(genre: str = "Action"):
    data= filmPeticions.getFilmsByGen(genre)
    return data

#RETORNA LES PELIS EN ORDRE ASC/DASC I SEGONS LA KEY. 
@app.get("/filmsOrder")
def getFilmsByOrder(field: str = "title", order: str = "asc"):
    userOrder = 1 if order == "asc" else -1
    data = filmPeticions.getFilmsByOrder(field, userOrder)
    return data

#RETORNA TANTES PELIS COM L'USUARI VULGUI. 
@app.get("/filmsLimit")
def getFilmsByLimit(limit: int):
    data = filmPeticions.getFilmsByLimit(limit)
    return data