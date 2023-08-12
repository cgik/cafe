from fastapi import UploadFile


async def upload_text(text: str | None = None):
    if not text:
        return {"message": "Text wasn't uploaded"}
    # parse text to make sure its not malicious
    # then save it to the database
    return {"text_output": text}


async def upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "File wasn't uploaded"}
    # parse file to make sure its not malicious
    # then save it to the database
    return {"filename": file.filename}
