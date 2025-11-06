from fastapi import FastAPI
from routers import director, pelicula, auth_director
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Routers
app.include_router(director.router)
app.include_router(pelicula.router)
app.include_router(auth_director.router)
app.mount("/static", StaticFiles(directory="static"), name="static")