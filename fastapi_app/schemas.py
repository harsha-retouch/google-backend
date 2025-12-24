from pydantic import BaseModel, Field, constr
from typing import Optional

# Aadhaar validation:
# - Exactly 12 digits
# - First digit cannot be 0 or 1
AADHAAR_REGEX = r"^[2-9]{1}[0-9]{11}$"


class VisitorBase(BaseModel):
    full_name: str = Field(..., max_length=100, description="Full Name")
    contact_number: str = Field(..., max_length=15, description="Contact Number")
    gender: str = Field(..., description="Gender")

    emergency_contact: Optional[str] = Field(
        None, max_length=15, description="Emergency Contact Number"
    )

    home_address: str = Field(..., description="Home Address")
    pin_code: str = Field(..., max_length=10, description="Pin Code")

    vehicle_number: Optional[str] = Field(
        None, max_length=20, description="Vehicle Number"
    )

    document_type: str = Field(..., description="Document Type (Aadhaar)")

    aadhaar_number: constr(
        regex=AADHAAR_REGEX,
        min_length=12,
        max_length=12
    )


class VisitorCreate(VisitorBase):
    """Schema used while creating a visitor"""
    pass


class VisitorResponse(VisitorBase):
    id: int

    face_photo_url: str
    aadhaar_document_url: str
    aadhaar_document_format: str  # image / pdf

    class Config:
        orm_mode = True
