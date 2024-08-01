import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
    if ENVIRONMENT == "docker":
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI_DOCKER")
    else:
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI_LOCAL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
