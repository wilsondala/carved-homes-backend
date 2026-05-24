from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.home_content import HomeContent
from app.schemas.home_content import (
    HomeContentCreate,
    HomeContentResponse,
    HomeContentUpdate,
)

router = APIRouter()


@router.get("/", response_model=HomeContentResponse | None)
def get_home_content(db: Session = Depends(get_db)):
    return db.query(HomeContent).filter(HomeContent.is_active == True).first()


@router.post("/", response_model=HomeContentResponse)
def create_home_content(
    payload: HomeContentCreate,
    db: Session = Depends(get_db)
):
    content = HomeContent(**payload.model_dump())

    db.add(content)
    db.commit()
    db.refresh(content)

    return content


@router.put("/{content_id}", response_model=HomeContentResponse)
def update_home_content(
    content_id: int,
    payload: HomeContentUpdate,
    db: Session = Depends(get_db)
):
    content = db.query(HomeContent).filter(HomeContent.id == content_id).first()

    for key, value in payload.model_dump().items():
        setattr(content, key, value)

    db.commit()
    db.refresh(content)

    return content