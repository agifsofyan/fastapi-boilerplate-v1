from app.core.exceptions.base_exception import AppException
from app.domain.entities.interest_entity import Interest
from app.domain.repositories.interest_repository import InterestRepository
from app.schemas.interest_schema import InterestCreate, InterestUpdate


class InterestNotFoundException(AppException):
    def __init__(self):
        super().__init__(status_code=404, message="Interest not found")


class InterestAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(status_code=400, message="Interest with this code already exists")


class InterestService:

    def __init__(self, repository: InterestRepository):
        self.repository = repository

    def create(self, request: InterestCreate) -> Interest:
        existing = self.repository.get_all()
        
        for interest in existing:
            if interest.code == request.code:
                raise InterestAlreadyExistsException()

        interest = Interest(
            id=None,
            name=request.name,
            code=request.code,
        )

        return self.repository.create(interest)

    def get_all(self) -> list[Interest]:
        return self.repository.get_all()

    def get_by_id(self, id: int) -> Interest:
        interest = self.repository.get_by_id(id)

        if interest is None:
            raise InterestNotFoundException()

        return interest

    def update(self, id: int, request: InterestUpdate) -> Interest:
        interest = self.repository.get_by_id(id)

        if interest is None:
            raise InterestNotFoundException()

        if request.name is not None:
            interest.name = request.name

        if request.code is not None:
            interest.code = request.code

        return self.repository.update(interest)

    def delete(self, id: int) -> None:
        interest = self.repository.get_by_id(id)

        if interest is None:
            raise InterestNotFoundException()

        self.repository.delete(id)
