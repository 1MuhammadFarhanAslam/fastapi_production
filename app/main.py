
# app/main.py
from fastapi import FastAPI
from app.api.v1.router import router as api_v1_router
from app.core.config import settings
from app.db.session import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# Include v1 API router
app.include_router(api_v1_router, prefix=settings.API_V1_PREFIX)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Production App"}
