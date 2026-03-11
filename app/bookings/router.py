from fastapi import APIRouter
from app.bookings.schemas import SBooking

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("")
def add_bookings(booking: SBooking):
    return {"message": "Бронирование создано", "data": booking}
