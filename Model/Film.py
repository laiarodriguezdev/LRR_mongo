from pydantic import BaseModel

class Film(BaseModel):
    title:str
    director:str 
    year:int
    genre:str
    rating:int
    country: str
