import cafe.common.messanger as messanger

from fastapi import APIRouter, UploadFile

upload_service_router = APIRouter()


@upload_service_router.post("/upload/file")
async def upload_file(file: UploadFile) -> dict[str, str]:
    return await upload_file(file)


@upload_service_router.post("/upload/text")
async def upload_text(text: str) -> dict[str, str]:
    messanger.pub_message("upload", text)
    return await upload_text(text)
