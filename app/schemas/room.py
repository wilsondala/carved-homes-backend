from datetime import datetime

from pydantic import BaseModel


class RoomBase(BaseModel):
    title: str
    description: str | None = None

    property_type: str = "Apartment"

    city: str = "Johannesburg"
    state: str = "Gauteng"
    country: str = "South Africa"
    address: str | None = None

    price_per_night: float

    guests: int = 1
    bedrooms: int = 1
    bathrooms: int = 1

    image_url: str | None = None
    video_url: str | None = None

    gallery_images: str | None = None
    gallery_videos: str | None = None

    upload_folder: str | None = None

    has_wifi: bool = True
    has_parking: bool = True
    has_pool: bool = False
    has_air_conditioning: bool = True

    available: bool = True


class RoomCreate(RoomBase):
    pass


class RoomResponse(RoomBase):
    id: int
    rating_average: float = 0
    rating_count: int = 0
    created_at: datetime

    class Config:
        from_attributes = True