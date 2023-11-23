from datetime import date, datetime, timedelta
from typing import List

from fastapi import Query

from app.hotels.rooms.dao import RoomDAO
from app.hotels.rooms.schemas import SRoomInfo
from app.hotels.router import router


@router.get("/{hotel_id}/rooms")
async def get_rooms_by_time(
        hotel_id: int,
        data_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
        data_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
) -> List[SRoomInfo]:
    rooms = await RoomDAO.get_all(hotel_id, data_from, data_to)
    return rooms