from app.bookings.models import Bookings
from sqlalchemy import select, and_, or_, func, insert
from app.dao.base import BaseDAO
from datetime import date

from app.database import engine, async_session_maker
from app.hotels.rooms.models import Rooms


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls,
                  user_id: int,
                  room_id: int,
                  data_from: date,
                  data_to: date,
                  ):
        # async with engine.connect() as session:
        #     booked_rooms = select(Bookings).where(
        #         and_(
        #             Bookings.room_id == 1,
        #             or_(
        #                 and_(Bookings.data_from >= data_from,
        #                      Bookings.data_from <= data_to
        #                      ),
        #                 and_(Bookings.data_from <= data_from,
        #                      Bookings.data_to > data_from)
        #             ),
        #
        #         )
        #     ).cte('booked_rooms')
        #
        #     get_rooms_left = select(
        #         (Rooms.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
        #     ).select_from(Rooms).join(
        #         booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
        #     ).where(Rooms.id == 1).group_by(
        #         Rooms.quantity, booked_rooms.c.room_id
        #     )
        #
        #     # print(get_rooms_left.compile(compile_kwargs={"literal_binds": True}))
        #
        #     rooms_left = await session.execute(get_rooms_left)
        #     rooms_left = rooms_left.scalar()
        #
        #     if not rooms_left or rooms_left > 0:
        #         get_price = select(
        #             Rooms.price).filter_by(id=room_id)
        #         price = await session.execute(get_price)
        #         price: int = price.scalar()
        #         add_booking = insert(Bookings).values(
        #             room_id=room_id,
        #             user_id=user_id,
        #             data_from=data_from,
        #             data_to=data_to,
        #             price=price
        #         ).returning(Bookings)
        #         print(add_booking)
        #         new_booking = await session.execute(add_booking)
        #         print(new_booking)
        #         await session.commit()
        #         return new_booking.scalar()
        #     else:
        #         return None
        async with async_session_maker() as session:
            booked_rooms = (
                select(Bookings)
                .where(
                    and_(
                        Bookings.data_from <= data_to,
                        Bookings.data_to >= data_from,
                        Bookings.room_id == room_id,
                    )
                )
                .cte("booked_rooms")
            )
            get_rooms_left = (
                select(
                    (Rooms.quantity - func.count(booked_rooms.c.room_id)).label(
                        "rooms_left"
                    )
                )
                .select_from(Rooms)
                .join(
                    booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
                )
                .where(Rooms.id == room_id)
                .group_by(Rooms.id, booked_rooms.c.room_id)
            )
            rooms_left = await session.execute(get_rooms_left)
            rooms_left: int = rooms_left.scalar()
            if not rooms_left or rooms_left > 0:
                get_price = select(Rooms.price).where(Rooms.id == room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                add_booking = (
                    insert(Bookings)
                    .values(
                        room_id=room_id,
                        user_id=user_id,
                        data_from=data_from,
                        data_to=data_to,
                        price=price,
                    )
                    .returning(Bookings.__table__.columns)
                )
                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.mappings().one_or_none()
            else:
                return None
