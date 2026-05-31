from .base_settings import *
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    "default": dj_database_url.parse(
        os.getenv("DATABASE_URL")
    )
}

DEBUG = False

CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = ["*"]

# CORS_ALLOWED_ORIGINS = []

