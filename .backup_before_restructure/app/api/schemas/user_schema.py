from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr  # Validates email format
    password: str = Field(..., min_length=8, max_length=72)  # Bcrypt limit

class UserResponse(BaseModel):
    id: int
    name: str
    email: str