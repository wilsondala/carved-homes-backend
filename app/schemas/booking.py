from datetime import date

from pydantic import BaseModel, EmailStr


class BookingCreate(BaseModel):
    room_id: int

    guest_name: str
    guest_email: EmailStr
    guest_phone: str | None = None

    guest_country: str
    guest_city: str | None = None

    check_in: date
    check_out: date

    guests_count: int = 1

    total_price: float

    currency: str = "USD"

    payment_method: str | None = None


class BookingResponse(BookingCreate):
    id: int
    payment_status: str
    status: str

    class Config:
        from_attributes = True