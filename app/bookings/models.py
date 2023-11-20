from app.database import Base
from sqlalchemy import JSON, Column, Computed, Date, ForeignKey, Integer, String


class Bookings(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    data_from = Column(Date, nullable=False)
    data_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed("(data_to - data_from) * price"))
    total_days = Column(Integer, Computed("(data_to - data_from)"))
