from typing import Union
from fastapi import FastAPI
from Model.Film import Film
from db import filmConnection
from db import filmPeticions

app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/films")
def getFilms():
    data = filmPeticions.getAllFilms()
    return data

@app.get("/filmsGenre")
def getFilmsByGen(genre: str = "Action"):
    data= filmPeticions.getFilmsByGen(genre)
    return data

