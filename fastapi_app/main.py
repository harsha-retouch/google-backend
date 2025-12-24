from fastapi import FastAPI

from config import settings
from models import Base
from database import engine
from api.v1.form import router as visitor_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Visitor Registration API",
    debug=settings.DEBUG
)

app.include_router(
    visitor_router,
    prefix="/api/v1"
)

@app.get("/")
def health_check():
    return {"status": "API is running"}
