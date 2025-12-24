import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
    SECRET_KEY = os.getenv("SECRET_KEY", "secret-key-change-me")

settings = Settings()