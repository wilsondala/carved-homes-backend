from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.booking import Booking
from app.services.whatsapp_service import (
    build_booking_whatsapp_message,
    build_whatsapp_link,
)

router = APIRouter()


@router.get("/booking/{booking_id}")
def booking_whatsapp_link(
    booking_id: int,
    phone: str,
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    message = build_booking_whatsapp_message(booking)
    link = build_whatsapp_link(phone, message)

    return {
        "booking_id": booking.id,
        "phone": phone,
        "message": message,
        "whatsapp_link": link,
    }