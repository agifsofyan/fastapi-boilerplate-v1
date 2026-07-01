from app.domain.entities.user import User
from app.shared.security.password import hash_password

class CreateUser:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, name: str, email: str, password: str) -> User:
        existing_user = self.user_repository.get_by_email(email)
        if existing_user:
            raise ValueError("Email already in use")

        
        hashed_password = hash_password(password)
        new_user = User(id=None, name=name, email=email, password=hashed_password)
        return self.user_repository.save(new_user)