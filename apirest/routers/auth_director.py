from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash

# Definimos el algoritmo de encriptación
ALGORITHM = "HS256"

# Duración del token
ACCESS_TOKEN_EXPIRE_MINUTES = 1

# Clave que se utilizará como semilla para generar el token
# openssl rand -hex 32
SECRET_KEY = "87ab51098990feb4a2f78da9c911187a71290ebd9e98e56d8b24090815f2ce6f"

# Objeto que se utilizará para el cálculo del hash y
# la verificación de las contraseñas
password_hash = PasswordHash.recommended()

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class Director(BaseModel):
    username : str
    fullname : str
    email : str
    disabled : bool
    
class DirectorBD(Director):
    password : str
    
users_db = {
    "rubencf" : {
        "username" : "rubencf",
        "fullname" : "Ruben Carrasco",
        "email" : "rubencarrasco@gmail.com",
        "disabled" : False,
        "password" : "123456"
    },
    "rubencf4" : {
        "username": "rubencf4",
        "fullname": "Ruben Carrasco",
        "email": "rubencarrasco@gmail.com",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$Lw2DEnh8Ynf16dpd3t4H1w$z1Df3PBP9gSRSiP/1TAi/xTqHl0hbO65Zy/DpmdUDd4"
    }
}

@router.post("/register", status_code=201)
def add_user(user: DirectorBD):
    if user.username not in users_db:
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.username] = user
        return user
    else:
        raise HTTPException(status_code=409, detail="User already exists")