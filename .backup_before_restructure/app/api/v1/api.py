from fastapi import APIRouter
from app.api.v1.routes import user_router

api_router = APIRouter()
api_router.include_router(user_router.router, prefix="/public", tags=["users"])