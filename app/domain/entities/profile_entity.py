from dataclasses import dataclass
from datetime import date
from app.schemas.user.profile_schema import Gender

@dataclass
class Profile:
    id: int | None
    user_id: int
    gender: Gender
    birth_date: date | None
    hobbies: list[str]
    phone_numbers: list[str]