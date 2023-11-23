from fastapi import APIRouter, Depends
from datetime import date

from app.tasks.tasks import send_email

from pydantic import parse_obj_as

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.exceptions import RoomCanNotBeBookedException
from app.users.dependecies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование проживания"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):  # -> list[SBooking]:
    return await BookingDAO().find_all(user_id=user.id)


@router.post("")
async def add_booking(
        room_id: int,
        data_from: date,
        data_to: date,
        user: Users = Depends(get_current_user),
):
    booking = await BookingDAO().add(user.id, room_id, data_from, data_to)
    booking_dict = parse_obj_as(SBooking, booking).dict()
    send_email.delay(booking_dict, user.email)
    return booking_dict
