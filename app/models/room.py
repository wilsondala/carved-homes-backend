from sqlalchemy import Column, Integer, String, Float, Boolean, Text

from app.database.session import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    property_type = Column(String, nullable=False, default="Apartment")

    city = Column(String, nullable=False, default="Johannesburg")
    state = Column(String, nullable=False, default="Gauteng")
    country = Column(String, nullable=False, default="South Africa")
    address = Column(String, nullable=True)

    price_per_night = Column(Float, nullable=False)

    guests = Column(Integer, nullable=False, default=1)
    bedrooms = Column(Integer, nullable=False, default=1)
    bathrooms = Column(Integer, nullable=False, default=1)

    image_url = Column(String, nullable=True)
    video_url = Column(String, nullable=True)

    gallery_images = Column(Text, nullable=True)
    gallery_videos = Column(Text, nullable=True)

    rating_average = Column(Float, default=0)
    rating_count = Column(Integer, default=0)

    has_wifi = Column(Boolean, default=True)
    has_parking = Column(Boolean, default=True)
    has_pool = Column(Boolean, default=False)
    has_air_conditioning = Column(Boolean, default=True)

    available = Column(Boolean, default=True)