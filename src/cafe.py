from fastapi import FastAPI

description = """
Integrative complexity analysis of social media accounts and texts
"""

api = FastAPI(
    title="cafe",
    description=description,
)

@api.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"message": "Hello World!"}