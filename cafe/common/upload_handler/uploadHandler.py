from fastapi import UploadFile


async def upload_text(text: str | None = None) -> dict[str, str]:
    if not text:
        return {"message": "Text wasn't uploaded"}
    # TODO: parse text to make sure its not malicious then save it to the database
    return {"text_output": text}


async def upload_file(file: UploadFile | None = None) -> dict[str, str]:
    if not file:
        return {"message": "File wasn't uploaded"}
    # TODO: parse file to make sure its not malicious then save it to the database
    return {"filename": file.filename}
