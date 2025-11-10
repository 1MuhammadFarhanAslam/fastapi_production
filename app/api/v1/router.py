# app/api/v1/router.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "FastAPI Production App is running!"}
