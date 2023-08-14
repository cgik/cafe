from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from cafe.features.routes.routesHandler import api_router
# from cafe.common.data.mysql import SessionLocal

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


api.include_router(api_router, prefix="/api")


@api.on_event("startup")
def on_startup() -> None:
    # db = SessionLocal()
    pass


@api.get("/health", tags=["health"])
def index() -> dict[str, str]:
    return {"message": "Hello World!"}
