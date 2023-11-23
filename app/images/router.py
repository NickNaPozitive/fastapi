from fastapi import APIRouter, UploadFile
import shutil

router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"],
)


@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
    with open(f"app/static/images/{name}.webp", "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
