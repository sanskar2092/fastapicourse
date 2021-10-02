import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path("/home/akumar/Work/personal/fastapicourse/jobboard/backend/.env")
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Job Board"
    PROJECT_VERSION: str = "0.1.2"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "course_db")
    DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
