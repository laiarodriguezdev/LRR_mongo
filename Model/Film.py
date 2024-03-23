from pydantic import BaseModel

class Film(BaseModel):
    title:str
    director:str 
    year:int
    genere:str
    rating:int
    country: str
