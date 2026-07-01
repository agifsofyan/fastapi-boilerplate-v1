from fastapi import APIRouter, Depends, HTTPException, status
from app.application.services.me_service import UserService
from app.application.services.profile.profile_service import ProfileService
from app.core.dependencies import get_current_user, get_create_profile_service, get_me_service, get_update_profile_service, get_delete_profile_service
from app.domain.entities.user_entity import User
from app.schemas.user.profile_schema import ProfileCreate, ProfileUpdate, ProfileResponse

router = APIRouter(prefix="/profiles")

@router.post("/", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
def create_profile(
    request: ProfileCreate,
    current_user: User = Depends(get_current_user),
    service: ProfileService = Depends(get_create_profile_service),
):
    if current_user.id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    user_id = current_user.id
    return service.create(user_id, request)
    
@router.get("/me")
def get_profile(
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_me_service),
):
    return service.me(current_user.id)

@router.put("/me", response_model=ProfileResponse)
def update_profile(
    request: ProfileUpdate,
    current_user: User = Depends(get_current_user),
    service: ProfileService = Depends(get_update_profile_service),
):
    if current_user.id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    return service.update(current_user.id, request)

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(
    current_user: User = Depends(get_current_user),
    service: ProfileService = Depends(get_delete_profile_service),
):
    if current_user.id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    service.delete(current_user.id)
