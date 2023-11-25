from sqladmin import ModelView

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.users.models import Users


class UserAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class BookingsAdmin(ModelView, model=Bookings):
    # column_list = [c.name for c in Bookings.__table__.c] + [Bookings.user]
    column_list = "__all__"
    name = "Букинг"
    name_plural = "Букинги"
    icon = "fa-solid fa-book"

    page_size = 100
    page_size_options = [50, 100, 200, 500]


class HotelsAdmin(ModelView, model=Hotels):
    column_list = "__all__"
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-hotel"


class RoomsAdmin(ModelView, model=Rooms):
    column_list = "__all__"
    name = "Номер"
    name_plural = "Номера"
    icon = "fa-solid fa-bed"
