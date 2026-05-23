from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.review import Review
from app.models.room import Room
from app.schemas.review import ReviewCreate, ReviewResponse

router = APIRouter()


@router.post("/", response_model=ReviewResponse)
def create_review(review_data: ReviewCreate, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == review_data.room_id).first()

    if not room:
        raise HTTPException(status_code=404, detail="Quarto não encontrado")

    review = Review(**review_data.model_dump())

    db.add(review)
    db.commit()
    db.refresh(review)

    reviews = db.query(Review).filter(Review.room_id == review_data.room_id).all()

    room.rating_count = len(reviews)
    room.rating_average = round(sum(r.rating for r in reviews) / len(reviews), 2)

    db.commit()
    db.refresh(room)

    return review


@router.get("/room/{room_id}", response_model=list[ReviewResponse])
def list_room_reviews(room_id: int, db: Session = Depends(get_db)):
    return db.query(Review).filter(Review.room_id == room_id).all()