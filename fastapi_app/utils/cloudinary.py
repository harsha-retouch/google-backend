import cloudinary
import cloudinary.uploader
from config import settings

# Cloudinary config (already correct)
cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET_KEY,
    secure=True
)

def upload_to_cloudinary(file, folder: str, resource_type="auto"):
    try:
        # 🔥 VERY IMPORTANT (Windows fix)
        file.seek(0)

        result = cloudinary.uploader.upload(
            file,
            folder=folder,
            resource_type=resource_type,
            timeout=180,             # ⬅️ prevent timeout
            chunk_size=6_000_000     # ⬅️ prevent connection reset
        )

        return result["secure_url"]

    except Exception as e:
        print("❌ Cloudinary upload failed:", e)
        raise
