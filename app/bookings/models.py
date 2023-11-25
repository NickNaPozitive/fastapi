from datetime import date

from app.database import Base
from sqlalchemy import Column, Computed, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.hotels.rooms.models import Rooms
from app.users.models import Users


class Bookings(Base):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    data_from: Mapped[date] = mapped_column(Date)
    data_to: Mapped[date] = mapped_column(Date)
    price: Mapped[int]
    total_cost: Mapped[int] = mapped_column(Computed("(data_to - data_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("data_to - data_from"))

    user: Mapped["Users"] = relationship(back_populates="bookings")
    room: Mapped["Rooms"] = relationship(back_populates="bookings")

    def __str__(self):
        return f"Booking #--->{self.id}"
