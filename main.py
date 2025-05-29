from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def bienvenue():
    try:
        return {"message": "Bienvenue sur l'API FastAPI avec CORS"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Une erreur s'est produite : {str(e)}")


@app.get("/test")
async def bonjour():
    try:
        return {"message": "Bonjour sur l'API FastAPI avec CORS"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Une erreur s'est produite : {str(e)}")
