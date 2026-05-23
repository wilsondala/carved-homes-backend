from datetime import datetime
from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    room_id: int
    guest_name: str
    rating: float = Field(ge=1, le=5)
    comment: str | None = None


class ReviewResponse(ReviewCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True