import pymongo

#AQUEST FITXER NOMÉS S'ENCARREGA DE CONECTAR-SE AMB LA BBDD. 
def db():
    try:
        return pymongo.MongoClient("mongodb://localhost:27017/").films
    except Exception as e:
        print(f"ERROR BBDD: {e}")