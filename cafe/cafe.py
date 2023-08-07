from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import settings

# from features.parsing.interface.parsing import router as parsing_router

description = """
Integrative Complexity Analysis of Texts
"""

api = FastAPI(
    title="cafe",
    description=description,
    version=settings.poetry.version
)

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST, GET, OPTIONS"],
    allow_headers=["*"]
)


# api.include_router(parsing_router)

@api.on_event("startup")
def on_startup():
    pass


@api.get("/healthz")
def index():
    return {"message": "Hello World!"}
