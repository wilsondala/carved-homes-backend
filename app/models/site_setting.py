from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.database.session import Base


class SiteSetting(Base):
    __tablename__ = "site_settings"

    id = Column(Integer, primary_key=True, index=True)

    site_name = Column(String, default="Carved Homes")
    logo_url = Column(String, nullable=True)

    default_language = Column(String, default="en")
    default_currency = Column(String, default="ZAR")
    dark_mode_default = Column(Boolean, default=True)

    whatsapp_number = Column(String, nullable=True)
    contact_email = Column(String, nullable=True)
    contact_phone = Column(String, nullable=True)

    address = Column(String, nullable=True)

    instagram_url = Column(String, nullable=True)
    facebook_url = Column(String, nullable=True)
    tiktok_url = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())