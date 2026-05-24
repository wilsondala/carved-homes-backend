from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingResponse
from datetime import timedelta

router = APIRouter()


def get_booking_or_404(booking_id: int, db: Session):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Reserva não encontrada"
        )

    return booking


@router.post("/", response_model=BookingResponse)
def create_booking(
    booking_data: BookingCreate,
    db: Session = Depends(get_db)
):
    booking = Booking(**booking_data.model_dump())

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking


@router.get("/", response_model=list[BookingResponse])
def list_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).order_by(Booking.id.desc()).all()


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    return get_booking_or_404(booking_id, db)


@router.patch("/{booking_id}/confirm", response_model=BookingResponse)
def confirm_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = get_booking_or_404(booking_id, db)

    booking.status = "confirmed"

    db.commit()
    db.refresh(booking)

    return booking


@router.patch("/{booking_id}/cancel", response_model=BookingResponse)
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = get_booking_or_404(booking_id, db)

    booking.status = "cancelled"

    db.commit()
    db.refresh(booking)

    return booking


@router.patch("/{booking_id}/complete", response_model=BookingResponse)
def complete_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = get_booking_or_404(booking_id, db)

    booking.status = "completed"

    db.commit()
    db.refresh(booking)

    return booking


@router.patch("/{booking_id}/payment-paid", response_model=BookingResponse)
def mark_payment_paid(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = get_booking_or_404(booking_id, db)

    booking.payment_status = "paid"

    db.commit()
    db.refresh(booking)

    return booking


@router.patch("/{booking_id}/payment-pending", response_model=BookingResponse)
def mark_payment_pending(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = get_booking_or_404(booking_id, db)

    booking.payment_status = "pending"

    db.commit()
    db.refresh(booking)

    return booking


@router.delete("/{booking_id}")
def delete_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = get_booking_or_404(booking_id, db)

    db.delete(booking)
    db.commit()

    return {
        "message": "Reserva removida com sucesso"
    }
@router.get("/unavailable-dates/{room_id}")
def unavailable_dates(
    room_id: int,
    db: Session = Depends(get_db)
):
    bookings = (
        db.query(Booking)
        .filter(
            Booking.room_id == room_id,
            Booking.status != "cancelled"
        )
        .all()
    )

    blocked_dates = []

    for booking in bookings:
        current = booking.check_in

        while current < booking.check_out:
            blocked_dates.append(current.isoformat())
            current += timedelta(days=1)

    return blocked_dates