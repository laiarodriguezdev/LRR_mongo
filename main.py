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

