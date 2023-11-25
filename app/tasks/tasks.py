import smtplib

from app.config import settings
from app.tasks.celery import celery
# from app.logger import logger
from PIL import Image
from pathlib import Path
from pydantic import EmailStr

from app.tasks.email_templates import create_booking_confirmation_email


@celery.task
def process_pic(
        path: str,
):
    img_path = Path(path)
    img = Image.open(img_path)
    img_resized_1000_1500 = img.resize((1000, 1500))
    img_resized_200_100 = img.resize((200, 100))
    img_resized_1000_1500.save(f"app/static/images/resized_1000_1500_{img_path.name}", quality=95)
    img_resized_200_100.save(f"app/static/images/resized_200_100 _{img_path.name}", quality=95)


@celery.task
def send_booking_confirmation_email(
        booking: dict,
        email_to: EmailStr,
):
    print("получил задание")
    email_to_mock = settings.SMTP_USER
    msg_content = create_booking_confirmation_email(booking, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.sendmail(settings.SMTP_USER, email_to, msg_content.as_string())

