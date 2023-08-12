from typing import Annotated
from fastapi import File, UploadFile


async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


async def upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "File wasn't uploaded"}

    return {"filename": file.filename}
