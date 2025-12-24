from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VisitorBase(BaseModel):
    full_name: str
    contact_number: str
    gender: str
    emergency_contact: Optional[str] = None
    home_town_address: str
    pin_code: str
    vehicle_number: Optional[str] = None
    aadhaar_number: str

class VisitorCreate(VisitorBase):
    face_photo_base64: Optional[str] = None
    aadhaar_photo_base64: Optional[str] = None
    scanner_data: Optional[str] = None

class VisitorResponse(VisitorBase):
    id: int
    face_photo_url: Optional[str]
    aadhaar_photo_url: Optional[str]
    document_type: str
    created_at: datetime
    is_submitted: bool
    
    class Config:
        from_attributes = True