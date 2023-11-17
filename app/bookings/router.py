from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.bookings.models import Bookings
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование проживания"],
)

@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingDAO().find_all() 
