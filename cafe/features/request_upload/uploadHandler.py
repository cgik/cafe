from fastapi import UploadFile

async def upload_text(text: str | None = None) -> dict[str, str]:
    if not text:
        return {"message": "No text was provided for analysis."}
    # TODO: parse text to make sure its not malicious then save it to the database
    return {"text_output": text}


async def upload_file(file: UploadFile | None = None) -> dict[str, str]:
    if not file:
        return {"message": "No file was provided for analysis."}
    # TODO: parse file to make sure its not malicious then save it to the database
    return {"filename": file.filename}
