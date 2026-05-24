from collections import defaultdict
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.booking import Booking

router = APIRouter()


@router.get("/dashboard")
def analytics_dashboard(
    db: Session = Depends(get_db)
):
    total_bookings = db.query(Booking).count()

    confirmed_bookings = (
        db.query(Booking)
        .filter(Booking.status == "confirmed")
        .count()
    )

    pending_bookings = (
        db.query(Booking)
        .filter(Booking.status == "pending")
        .count()
    )

    cancelled_bookings = (
        db.query(Booking)
        .filter(Booking.status == "cancelled")
        .count()
    )

    paid_bookings = (
        db.query(Booking)
        .filter(Booking.payment_status == "paid")
        .count()
    )

    total_revenue = (
        db.query(func.sum(Booking.total_price))
        .filter(Booking.payment_status == "paid")
        .scalar()
    )

    if total_revenue is None:
        total_revenue = 0

    bookings = db.query(Booking).all()

    monthly_revenue = defaultdict(float)
    monthly_bookings = defaultdict(int)

    for booking in bookings:
        try:
            if booking.created_at:
                month = booking.created_at.strftime("%b")

                monthly_bookings[month] += 1

                if booking.payment_status == "paid":
                    monthly_revenue[month] += float(
                        booking.total_price or 0
                    )

        except Exception:
            pass

    revenue_chart = [
        {
            "month": month,
            "revenue": value
        }
        for month, value in monthly_revenue.items()
    ]

    bookings_chart = [
        {
            "month": month,
            "bookings": value
        }
        for month, value in monthly_bookings.items()
    ]

    occupancy_rate = 0

    if total_bookings > 0:
        occupancy_rate = round(
            (confirmed_bookings / total_bookings) * 100,
            2
        )

    latest_bookings = (
        db.query(Booking)
        .order_by(Booking.id.desc())
        .limit(8)
        .all()
    )

    return {
        "total_bookings": total_bookings,
        "confirmed_bookings": confirmed_bookings,
        "pending_bookings": pending_bookings,
        "cancelled_bookings": cancelled_bookings,
        "paid_bookings": paid_bookings,
        "total_revenue": total_revenue,
        "occupancy_rate": occupancy_rate,
        "monthly_revenue": revenue_chart,
        "monthly_bookings": bookings_chart,
        "latest_bookings": [
            {
                "id": booking.id,
                "guest_name": booking.guest_name,
                "total_price": booking.total_price,
                "currency": booking.currency,
                "status": booking.status,
                "payment_status": booking.payment_status,
            }
            for booking in latest_bookings
        ]
    }