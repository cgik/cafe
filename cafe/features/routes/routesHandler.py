from fastapi import APIRouter

from cafe.features.request_upload.requestUploadService import upload_service_router

api_router = APIRouter()

api_router.include_router(upload_service_router, prefix="/v1", tags=["upload"])
