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
    DATABASE_URL: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    ACCESS_TOKEN_EXPIRE_MINUTE: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTE"))
    ALGORITHM: str = os.getenv("ALGORITHM")
    SECRET_KEY: str = os.getenv("SECRET_KEY")

    TEST_USER_EMAIL = "test@example.com"


settings = Settings()
