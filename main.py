from typing import Union
from fastapi import FastAPI
from db import film
from db import filmPeticions

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/films")
def getFilms():
    film.db()
    data = filmPeticions.consulta()
    return data

