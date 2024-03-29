import uvicorn

from cafe.config import settings


def run(
        port: int = settings.server.port,
        host: str = settings.server.host,
        log_level: str = settings.server.log_level,
        reload: bool = settings.server.reload,
):
    uvicorn.run(
        "cafe.api:api",
        host=host,
        port=port,
        log_level=log_level,
        reload=reload,
    )
