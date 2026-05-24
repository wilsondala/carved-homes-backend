from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException
from jose import jwt
from pydantic import BaseModel

from app.core.config import settings

router = APIRouter()


class AdminLoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
def admin_login(data: AdminLoginRequest):
    if data.email != settings.ADMIN_EMAIL or data.password != settings.ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    payload = {
        "sub": data.email,
        "role": "admin",
        "exp": datetime.utcnow() + timedelta(days=7),
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": "admin",
    }