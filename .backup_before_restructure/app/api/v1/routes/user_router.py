from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.application.services.create_user import CreateUser
from app.api.schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_repository = UserRepositoryImpl(db)
    create_user_use_case = CreateUser(user_repository)
    new_user = create_user_use_case.execute(name=user.name, email=user.email, password=user.password)
    return UserResponse(id=new_user.id, name=new_user.name, email=new_user.email)