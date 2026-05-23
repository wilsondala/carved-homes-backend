from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.database.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    phone = Column(String, nullable=True)

    avatar = Column(String, nullable=True)

    bio = Column(String, nullable=True)

    location = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())