from fastapi import APIRouter, UploadFile
import shutil

from app.tasks.tasks import process_pic

router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"],
)


@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
    img_path = f"app/static/images/{name}.webp"
    with open(img_path, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    process_pic.delay(img_path)
