import cloudinary
import cloudinary.uploader
from app.core.config import settings
import base64
from io import BytesIO

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
    secure=True
)

class CloudinaryService:
    @staticmethod
    def upload_base64_image(base64_string: str, folder: str = "visitors") -> str:
        """Upload base64 image to Cloudinary"""
        try:
            # Remove data URL prefix if present
            if ',' in base64_string:
                base64_string = base64_string.split(',')[1]
            
            # Decode base64
            image_data = base64.b64decode(base64_string)
            
            # Upload to Cloudinary
            upload_result = cloudinary.uploader.upload(
                BytesIO(image_data),
                folder=folder
            )
            
            return upload_result.get('secure_url', '')
        except Exception as e:
            print(f"Cloudinary upload error: {e}")
            return ""