from fastapi import APIRouter
from app.api.v1.users import router as users_router
from app.api.v1.health import router as health_router
from app.api.v1.rooms import router as rooms_router
from app.api.v1.bookings import router as bookings_router
from app.api.v1.reviews import router as reviews_router
from app.api.v1.payments import router as payments_router
from app.api.v1.webhooks import router as webhooks_router

api_router = APIRouter()

api_router.include_router(health_router, tags=["Health"])

api_router.include_router(
    rooms_router,
    prefix="/rooms",
    tags=["Rooms"]
)

api_router.include_router(
    bookings_router,
    prefix="/bookings",
    tags=["Bookings"]
)

api_router.include_router(
    reviews_router,
    prefix="/reviews",
    tags=["Reviews"]
)

api_router.include_router(
    payments_router,
    prefix="/payments",
    tags=["Payments"]
)

api_router.include_router(
    webhooks_router,
    prefix="/webhooks",
    tags=["Webhooks"]
)

api_router.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)