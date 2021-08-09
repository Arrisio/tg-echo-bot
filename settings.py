import sys
from pydantic import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_TG_ID: int



    LOG_LEVEL: str = "DEBUG"
    LOG_USE_JSON: bool = False

    DATABUS_API_URL: str = "http://10.124.6.10:8002"

    class Config:
        env_file: str = ".env"
        env_file_encoding = "utf-8"


loguru_config = {
    "handlers": [
        {
            "sink": sys.stdout,
            "level": Settings().LOG_LEVEL,
            "serialize": Settings().LOG_USE_JSON,
            "format": "<level>{level: <8} {time:YYYY-MM-DD HH:mm:ss}</level>|<cyan>{name:<12}</cyan>:<cyan>{function:<24}</cyan>:<cyan>{line}</cyan> - <level>{message:>32}</level> |{extra}",
        },
    ],
}

settings = Settings()