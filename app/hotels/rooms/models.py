from typing import Optional
from sqlalchemy import JSON, ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.bookings.models import Bookings
from app.database import Base
from app.hotels.models import Hotels


class Rooms(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)
