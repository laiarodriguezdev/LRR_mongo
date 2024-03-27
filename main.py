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
    return filmPeticions.getAllFilms()

#RETORNA LA PELI CORRESPONENT AL ID
@app.get("/films/{id}")
def getFilmById(id):
    return filmPeticions.getFilmById(id)

#CREA UN NOU DOCUMENT
@app.post("/film/")
def createFilm(film: Film):
    return filmPeticions.createFilm(film)

#ACTUALITZA UN NOU DOCUMENT/FILM. 
@app.put("/film/{id}")
def updateFilm(id, film:Film):
    return filmPeticions.updateFilm(id, film)

#ESBORRA EL DOCUMENT/FILM. 
@app.delete("/film/{id}")
def deleteFilm(id):
    return filmPeticions.deleteFilm(id)


#RETORNA LES PELIS DE ACTION, BIOGRAPHY, ETC. 
@app.get("/filmsGenre")
def getFilmsByGenre(genre: str = "Action"):
    return filmPeticions.getFilmsByGen(genre)

#RETORNA LES PELIS EN ORDRE ASC/DASC I SEGONS LA KEY. 
@app.get("/filmsOrder")
def getFilmsByOrder(field: str = "title", order: str = "asc"):
    userOrder = 1 if order == "asc" else -1
    return filmPeticions.getFilmsByOrder(field, userOrder)

#RETORNA TANTES PELIS COM L'USUARI VULGUI. 
@app.get("/filmsLimit")
def getFilmsByLimit(limit: int):
    return filmPeticions.getFilmsByLimit(limit)