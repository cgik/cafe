from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import settings

from features.upload.requestUploadService import upload_service_router

# from features.parsing.interface.parsing import router as parsing_router

description = """
Integrative Complexity Analysis of Texts
"""

api = FastAPI(
    title="cafe",
    description=description,
)

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST, GET, OPTIONS"],
    allow_headers=["*"]
)


api.include_router(upload_service_router)


@api.on_event("startup")
def on_startup():
    pass


@api.get("/healthz")
def index():
    return {"message": "Hello World!"}
