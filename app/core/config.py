from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Carved Homes API"

    DATABASE_URL: str

    SECRET_KEY: str = "super_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:5173"]

    JWT_SECRET_KEY: str = "super_secret_key"
    JWT_ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()