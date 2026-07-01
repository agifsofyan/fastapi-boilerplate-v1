from fastapi import APIRouter
from app.api.v1.routes import auth_router, profile_router, interest_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth_router.router, tags=["auth"])
api_router.include_router(profile_router.router, tags=["profile"])
api_router.include_router(interest_router.router, tags=["interests"])