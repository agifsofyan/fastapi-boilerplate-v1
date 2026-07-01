from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.db.models.user_model import UserModel

class UserRepositoryImpl(UserRepository):
    def __init__(self, db):
        self.db = db

    def save(self, user: User) -> User:
        db_user = UserModel(name=user.name, email=user.email, password=user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User(id=db_user.id, name=db_user.name, email=db_user.email, password=db_user.password)

    def get_by_id(self, user_id: int) -> User | None:
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            return User(id=db_user.id, name=db_user.name, email=db_user.email)
        return None

    def get_by_email(self, email: str) -> User | None:
        db_user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if db_user:
            return User(id=db_user.id, name=db_user.name, email=db_user.email)
        return None