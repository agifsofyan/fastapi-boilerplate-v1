"""FastAPI Application Entry Point"""
from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.core.exceptions.handlers import register_exception_handlers

app = FastAPI(
    title=settings.PROJECT_NAME if hasattr(settings, 'PROJECT_NAME') else "FastAPI Application",
    version="1.0.0",
    description="Clean Architecture FastAPI Application"
)

register_exception_handlers(app)

app.include_router(api_router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
