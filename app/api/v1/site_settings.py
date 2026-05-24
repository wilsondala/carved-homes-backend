from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.site_setting import SiteSetting
from app.schemas.site_setting import (
    SiteSettingCreate,
    SiteSettingResponse,
    SiteSettingUpdate,
)

router = APIRouter()


@router.get("/", response_model=SiteSettingResponse | None)
def get_site_settings(db: Session = Depends(get_db)):
    return db.query(SiteSetting).first()


@router.post("/", response_model=SiteSettingResponse)
def create_site_settings(
    payload: SiteSettingCreate,
    db: Session = Depends(get_db)
):
    settings = SiteSetting(**payload.model_dump())

    db.add(settings)
    db.commit()
    db.refresh(settings)

    return settings


@router.put("/{setting_id}", response_model=SiteSettingResponse)
def update_site_settings(
    setting_id: int,
    payload: SiteSettingUpdate,
    db: Session = Depends(get_db)
):
    settings = db.query(SiteSetting).filter(SiteSetting.id == setting_id).first()

    for key, value in payload.model_dump().items():
        setattr(settings, key, value)

    db.commit()
    db.refresh(settings)

    return settings