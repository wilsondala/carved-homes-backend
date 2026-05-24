from datetime import datetime
from pydantic import BaseModel


class SiteSettingBase(BaseModel):
    site_name: str = "Carved Homes"
    logo_url: str | None = None

    default_language: str = "en"
    default_currency: str = "ZAR"
    dark_mode_default: bool = True

    whatsapp_number: str | None = None
    contact_email: str | None = None
    contact_phone: str | None = None

    address: str | None = None

    instagram_url: str | None = None
    facebook_url: str | None = None
    tiktok_url: str | None = None


class SiteSettingCreate(SiteSettingBase):
    pass


class SiteSettingUpdate(SiteSettingBase):
    pass


class SiteSettingResponse(SiteSettingBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True