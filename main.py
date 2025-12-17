from fastapi import FastAPI

from proyecto.routers import director, pelicula, auth_director, director_db, pelicula_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Routers
app.include_router(director.router)
app.include_router(pelicula.router)
app.include_router(auth_director.router)
app.include_router(director_db.router)
app.include_router(pelicula_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static")