from fastapi import APIRouter

router = APIRouter()

@router.post("/scan")
async def scan_document():
    """Scan document"""
    return {"message": "Scanner endpoint", "status": "working"}

@router.get("/test")
async def test_scanner():
    return {"status": "scanner_working"}