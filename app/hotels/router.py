import asyncio
from datetime import date, datetime, timedelta
from typing import List, Optional
from pydantic import parse_obj_as

from fastapi import APIRouter, Query

from fastapi_cache.decorator import cache

from app.exceptions import CannotBookHotelForLongPeriod, DateFromCannotBeAfterDateTo
from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotel, SHotelInfo

router = APIRouter(prefix="/hotels", tags=["Отели"])


@router.get("/{location}")
@cache(expire=40)
async def get_hotels_by_location_and_time(
        location: str,
        data_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
        data_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
):
    await asyncio.sleep(3)
    # if data_from > data_to:
    #     raise DateFromCannotBeAfterDateTo
    # if (data_to - data_from).days > 31:
    #     raise CannotBookHotelForLongPeriod
    hotels = await HotelDAO.get_all(location, data_from, data_to)
    hotels_js = parse_obj_as(list[SHotelInfo], hotels)
    return hotels_js


@router.get("/id/{hotel_id}", include_in_schema=True)
async def get_hotel_by_id(
        hotel_id: int,
) -> Optional[SHotel]:
    return await HotelDAO.find_one_or_none(id=hotel_id)
