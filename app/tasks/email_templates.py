from pydantic import EmailStr

from email.message import EmailMessage

from app.config import settings


def create_booking_confirmation_email(
        booking: dict,
        email_to: EmailStr,
):
    email = EmailMessage()

    email["Subject"] = "Booking Confirmation"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Booking Confirmation</h1>
            Вы забронировали отель c {booking["data_from"]} по {booking["data_to"]}
        """,
        subtype="html",
    )
    return email
