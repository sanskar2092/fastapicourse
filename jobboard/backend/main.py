from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import sys
from core.config import settings
from db.session import engine
from db.base import Base
from loguru import logger
from apis.base import api_router
from webapps.base import api_router as webapp_router
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


def include_router(application):
    application.include_router(api_router)
    application.include_router(webapp_router)


def configure_static(application):
    application.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    logger.info("creating application instance")
    application = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(application)
    configure_static(application)
    return application


app = start_application()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
