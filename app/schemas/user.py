from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse