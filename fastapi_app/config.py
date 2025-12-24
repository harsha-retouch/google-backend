import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Settings:
    def __init__(self):
        self.DEBUG: bool = self._get_bool("DEBUG", False)

        self.DATABASE_URL: str = os.getenv("DATABASE_URL")

        self.CLOUDINARY_CLOUD_NAME: str = os.getenv("CLOUDINARY_CLOUD_NAME")
        self.CLOUDINARY_API_KEY: str = os.getenv("CLOUDINARY_API_KEY")
        self.CLOUDINARY_API_SECRET_KEY: str = os.getenv("CLOUDINARY_API_SECRET_KEY")

        # Upload directory (default: UPLOADS)
        self.UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "UPLOADS")

        # Ensure upload directory exists
        os.makedirs(self.UPLOAD_DIR, exist_ok=True)

    def _get_bool(self, key: str, default: bool) -> bool:
        value = os.getenv(key)
        if value is None:
            return default
        return value.lower() in ("true", "1", "yes")


# Single settings instance for entire app
settings = Settings()
