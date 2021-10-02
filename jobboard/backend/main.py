from fastapi import FastAPI
import sys
from core.config import settings
from core.session import engine
from core.base import Base
from loguru import logger
logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>",
)


def create_tables():
    logger.info("creating tables")
    Base.metadata.create_all(bind=engine)


def start_application():
    logger.info("creating application instance")
    application = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return application


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello"}
