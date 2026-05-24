from datetime import datetime
from pydantic import BaseModel


class HomeContentBase(BaseModel):
    hero_title_en: str = "Carved Homes"
    hero_title_pt: str = "Carved Homes"

    hero_subtitle_en: str | None = None
    hero_subtitle_pt: str | None = None

    hero_image_url: str | None = None
    hero_video_url: str | None = None

    featured_title_en: str = "Featured Rooms"
    featured_title_pt: str = "Quartos em Destaque"

    featured_video_url: str | None = None

    cta_title_en: str | None = None
    cta_title_pt: str | None = None

    cta_text_en: str | None = None
    cta_text_pt: str | None = None

    is_active: bool = True


class HomeContentCreate(HomeContentBase):
    pass


class HomeContentUpdate(HomeContentBase):
    pass


class HomeContentResponse(HomeContentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True