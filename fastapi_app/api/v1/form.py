from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from fastapi.concurrency import run_in_threadpool
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import Visitor
from database import SessionLocal
from utils.cloudinary import upload_to_cloudinary


router = APIRouter(tags=["Visitor Registration"])


# -------------------------
# Database dependency
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------
# File size validation
# -------------------------
def validate_file_size(upload_file: UploadFile, max_mb: int):
    upload_file.file.seek(0, 2)
    size = upload_file.file.tell()
    upload_file.file.seek(0)

    if size > max_mb * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail=f"File must be under {max_mb}MB"
        )


# -------------------------
# Visitor Registration API
# -------------------------
@router.post("/visitor/register")
async def register_visitor(
    full_name: str = Form(...),
    contact_number: str = Form(...),
    gender: str = Form(...),
    emergency_contact: str = Form(None),
    home_address: str = Form(...),
    pin_code: str = Form(...),
    vehicle_number: str = Form(None),

    document_type: str = Form(...),
    aadhaar_number: str = Form(...),

    face_photo: UploadFile = File(...),
    aadhaar_document: UploadFile = File(...),

    db: Session = Depends(get_db)
):
    # -------------------------
    # Upload Face Photo
    # -------------------------
    validate_file_size(face_photo, 2)

    face_url = await run_in_threadpool(
        upload_to_cloudinary,
        face_photo.file,
        "visitors/face",
        "image"
    )

    # -------------------------
    # Upload Aadhaar Document
    # -------------------------
    validate_file_size(aadhaar_document, 5)

    if aadhaar_document.filename.lower().endswith(".pdf"):
        resource_type = "raw"
        document_format = "pdf"
    else:
        resource_type = "image"
        document_format = "image"

    aadhaar_url = await run_in_threadpool(
        upload_to_cloudinary,
        aadhaar_document.file,
        "visitors/aadhaar",
        resource_type
    )

    # -------------------------
    # Save to Database
    # -------------------------
    visitor = Visitor(
        full_name=full_name,
        contact_number=contact_number,
        gender=gender,
        emergency_contact=emergency_contact,
        home_address=home_address,
        pin_code=pin_code,
        vehicle_number=vehicle_number,
        document_type=document_type,
        aadhaar_number=aadhaar_number,
        face_photo_url=face_url,
        aadhaar_document_url=aadhaar_url,
        aadhaar_document_format=document_format
    )

    try:
        db.add(visitor)
        db.commit()
        db.refresh(visitor)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Aadhaar number already exists"
        )

    return {
        "message": "Visitor registered successfully",
        "visitor_id": visitor.id
    }
