from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=72)


class UserUpdate(UserBase):
    password: str | None = Field(None, min_length=8, max_length=72)


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
