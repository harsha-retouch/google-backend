from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Visitor(Base):
    __tablename__ = "visitors"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100))
    contact_number = Column(String(15))
    gender = Column(String(10))
    emergency_contact = Column(String(15))
    home_town_address = Column(Text)
    pin_code = Column(String(10))
    vehicle_number = Column(String(20))
    face_photo_url = Column(Text)
    aadhaar_photo_url = Column(Text)
    document_type = Column(String(50), default="Aadhaar Card")
    aadhaar_number = Column(String(12))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_submitted = Column(Boolean, default=False)