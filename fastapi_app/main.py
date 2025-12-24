from fastapi import FastAPI

from config import settings
from models import Base
from database import engine
from api.v1.form import router as visitor_router
from fastapi.middleware.cors import CORSMiddleware

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Visitor Registration API",
    debug=settings.DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    visitor_router,
    prefix="/api/v1"
)

@app.get("/")
def health_check():
    return {"status": "API is running"}
