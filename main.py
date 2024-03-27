from typing import Union
from fastapi import FastAPI
from Model.Film import Film
from db import filmConnection
from db import filmPeticions

app = FastAPI()


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

#RETORNA LES PELIS DE ACTION, BIOGRAPHY, ETC. 
@app.get("/filmsGenre")
def getFilmsByGen(genre: str = "Action"):
    data= filmPeticions.getFilmsByGen(genre)
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
