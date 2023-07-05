from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from features.parsing.interface.parsing import router as parsing_router

description = """
Intergrative Complexity Analysis of Texts
"""

api = FastAPI(
    title="cafe",
    description=description,
    version="0.1.0"
)

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

api.include_router(parsing_router)

@api.on_event("startup")
def on_startup():
    pass
