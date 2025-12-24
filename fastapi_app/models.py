from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Visitor(Base):
    __tablename__ = "visitors"

    id = Column(Integer, primary_key=True, index=True)

    # Basic Details
    full_name = Column(String(100), nullable=False)
    contact_number = Column(String(15), nullable=False)
    gender = Column(String(10), nullable=False)

    emergency_contact = Column(String(15), nullable=True)

    # Address Details
    home_address = Column(Text, nullable=False)
    pin_code = Column(String(10), nullable=False)

    vehicle_number = Column(String(20), nullable=True)

    # Document Details
    document_type = Column(String(30), nullable=False)

    # Aadhaar (Unique)
    aadhaar_number = Column(
        String(12),
        nullable=False,
        unique=True,
        index=True
    )

    # Cloudinary URLs
    face_photo_url = Column(Text, nullable=False)

    aadhaar_document_url = Column(Text, nullable=False)
    aadhaar_document_format = Column(String(10), nullable=False)  # image / pdf
