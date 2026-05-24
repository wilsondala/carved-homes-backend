from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.booking import Booking

router = APIRouter()


@router.post("/create-checkout/{booking_id}")
def create_checkout(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    if booking.payment_status == "paid":
        return {
            "message": "Payment already completed",
            "checkout_url": f"/bookings/{booking.id}/success"
        }

    return {
        "booking_id": booking.id,
        "amount": booking.total_price,
        "currency": booking.currency,
        "payment_status": booking.payment_status,
        "checkout_url": f"/payment/mock/{booking.id}"
    }


@router.post("/mock-pay/{booking_id}")
def mock_pay(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    booking.payment_status = "paid"
    booking.status = "confirmed"

    db.commit()
    db.refresh(booking)

    return {
        "message": "Payment completed successfully",
        "booking_id": booking.id,
        "payment_status": booking.payment_status,
        "status": booking.status
    }