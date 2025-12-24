from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your modules
from app.core.database import engine, Base
from app.api.v1.endpoints import visitors, scanner
import logging
from sqlalchemy import text

logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="K Royal's PG Visitor Management",
    description="Visitor registration system with document scanning",
    version="1.0.0"
)

# Create tables and verify DB connection at startup
@app.on_event("startup")
def startup_event():
    try:
        Base.metadata.create_all(bind=engine)
        # quick connection check
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Database tables created and connection verified")
    except Exception as exc:
        logger.exception("Database initialization failed: %s", exc)
        raise

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(visitors.router, prefix="/api/v1/visitors", tags=["visitors"])
app.include_router(scanner.router, prefix="/api/v1/scanner", tags=["scanner"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to K Royal's PG Visitor Management System",
        "version": "1.0.0",
        "endpoints": {
            "visitors": "/api/v1/visitors/",
            "register": "/api/v1/visitors/register",
            "form_config": "/api/v1/visitors/form-config",
            "scanner": "/api/v1/scanner/scan"
        }
    }

@app.get("/health")
async def health_check():
    db_status = "unknown"
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as exc:
        db_status = f"error: {str(exc)}"
    return {"status": "healthy", "database": db_status}