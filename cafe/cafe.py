from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from features.request_upload.requestUploadService import upload_service_router

description = """
Integrative Complexity Analysis of Texts
"""

api = FastAPI(
    title="cafe",
    description=description,
    version="0.1.0",
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
