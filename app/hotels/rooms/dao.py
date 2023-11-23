from datetime import date

from sqlalchemy import and_, func, select

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.rooms.models import Rooms


class RoomDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def get_all(cls, hotel_id: int, data_from: date, data_to: date):
        async with async_session_maker() as session:
            booked_rooms = (
                select(func.count(Bookings.id).label("booked"), Bookings.room_id)
                .where(
                    and_(
                        Bookings.data_from <= data_to,
                        Bookings.data_to >= data_from,
                    )
                )
                .group_by(Bookings.room_id)
                .cte("booked_rooms")
            )

            get_rooms = (
                select(
                    Rooms.id,
                    Rooms.hotel_id,
                    Rooms.name,
                    Rooms.description,
                    Rooms.services,
                    Rooms.price,
                    Rooms.quantity,
                    Rooms.image_id,
                    ((data_to - data_from).days * Rooms.price).label("total_cost"),
                    (Rooms.quantity - func.coalesce(booked_rooms.c.booked, 0)).label(
                        "rooms_left"
                    ),
                )
                .select_from(Rooms)
                .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
                .where(
                    and_(
                        Rooms.quantity - func.coalesce(booked_rooms.c.booked, 0) > 0,
                        Rooms.hotel_id == hotel_id,
                    )
                )
            )
            rooms = await session.execute(get_rooms)
            return rooms.mappings().all()