from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.visitor import Visitor
from app.schemas.visitor import VisitorCreate, VisitorResponse

router = APIRouter()

@router.post("/register", response_model=VisitorResponse)
async def register_visitor(
    visitor: VisitorCreate,
    db: Session = Depends(get_db)
):
    """Register a new visitor"""
    db_visitor = Visitor(
        full_name=visitor.full_name,
        contact_number=visitor.contact_number,
        gender=visitor.gender,
        emergency_contact=visitor.emergency_contact,
        home_town_address=visitor.home_town_address,
        pin_code=visitor.pin_code,
        vehicle_number=visitor.vehicle_number,
        aadhaar_number=visitor.aadhaar_number,
        is_submitted=True
    )
    
    try:
        db.add(db_visitor)
        db.commit()
        db.refresh(db_visitor)
        return db_visitor
    except Exception as exc:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/", response_model=List[VisitorResponse])
async def get_visitors(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all visitors"""
    visitors = db.query(Visitor).offset(skip).limit(limit).all()
    return visitors

@router.get("/form-config")
async def get_form_config():
    """Get form configuration"""
    return {
        "fields": [
            {"name": "full_name", "label": "Full Name", "type": "text", "required": True},
            {"name": "contact_number", "label": "Contact Number", "type": "tel", "required": True},
            {"name": "gender", "label": "Gender", "type": "radio", "options": ["Male", "Female", "Other"], "required": True},
            {"name": "emergency_contact", "label": "Emergency Contact Number", "type": "tel", "required": False},
            {"name": "home_town_address", "label": "Home Town Address", "type": "textarea", "required": True},
            {"name": "pin_code", "label": "Pin Code", "type": "text", "required": True},
            {"name": "vehicle_number", "label": "Vehicle Number", "type": "text", "required": False},
            {"name": "face_photo", "label": "Face Photo", "type": "file", "accept": "image/*", "required": True},
            {"name": "aadhaar_photo", "label": "Aadhaar Document Photo", "type": "file", "accept": "image/*", "required": True},
            {"name": "document_type", "label": "Document Type", "type": "select", "options": ["Aadhaar Card"], "required": True},
            {"name": "aadhaar_number", "label": "Aadhaar Number", "type": "text", "required": True},
        ]
    }