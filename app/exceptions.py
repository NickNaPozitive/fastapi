from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует",
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неправильная почта или пароль",
)

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен истек",
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен отсутствует",
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неправильный формат токена",
)

UserIsNotPresentException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND
)

RoomCanNotBeBookedException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Комната не доступна для бронирования",
)

CannotBookHotelForLongPeriod = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Невозможно забронировать отель сроком более месяца",
)

DateFromCannotBeAfterDateTo = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Дата заезда не может быть позже даты выезда",
)
