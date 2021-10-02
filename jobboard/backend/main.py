from fastapi import FastAPI
import sys
from core.config import settings
from db.session import engine
from db.models.base import Base
from loguru import logger
from apis.base import api_router
import uvicorn

logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>",
)


def create_tables():
    logger.info("creating tables")
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    logger.info("creating application instance")
    application = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(application)
    return application


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
