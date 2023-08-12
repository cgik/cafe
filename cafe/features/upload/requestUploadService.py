import common.upload_handler.uploadHandler as uploadHandler
from fastapi import APIRouter, UploadFile

upload_service_router = APIRouter()


@upload_service_router.post("/upload/file")
async def upload_file(file: UploadFile):
    await uploadHandler.upload_file(file)


@upload_service_router.post("/upload/text")
async def upload_text(text: str):
    pass
