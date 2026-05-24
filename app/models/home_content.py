from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func

from app.database.session import Base


class HomeContent(Base):
    __tablename__ = "home_content"

    id = Column(Integer, primary_key=True, index=True)

    hero_title_en = Column(String, default="Carved Homes")
    hero_title_pt = Column(String, default="Carved Homes")

    hero_subtitle_en = Column(Text, nullable=True)
    hero_subtitle_pt = Column(Text, nullable=True)

    hero_image_url = Column(String, nullable=True)
    hero_video_url = Column(String, nullable=True)

    featured_title_en = Column(String, default="Featured Rooms")
    featured_title_pt = Column(String, default="Quartos em Destaque")

    cta_title_en = Column(String, nullable=True)
    cta_title_pt = Column(String, nullable=True)

    cta_text_en = Column(Text, nullable=True)
    cta_text_pt = Column(Text, nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())