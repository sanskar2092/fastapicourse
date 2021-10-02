from fastapi import FastAPI
from core.config import Settings

app = FastAPI(title=Settings.PROJECT_TITLE, version=Settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
    return {"detail": "Hello"}
