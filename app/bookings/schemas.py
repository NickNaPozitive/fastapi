from pydantic import BaseModel
from datetime import date

class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    data_from: date
    data_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        from_attributes = True