from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey

from app.database.session import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)

    guest_name = Column(String, nullable=False)
    guest_email = Column(String, nullable=False)
    guest_phone = Column(String, nullable=True)

    guest_country = Column(String, nullable=False)
    guest_city = Column(String, nullable=True)

    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)

    guests_count = Column(Integer, default=1)

    total_price = Column(Float, nullable=False)
    currency = Column(String, default="USD")

    payment_method = Column(String, nullable=True)
    payment_status = Column(String, default="pending")

    status = Column(String, default="pending")