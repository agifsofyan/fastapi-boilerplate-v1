from abc import ABC, abstractmethod
from app.domain.entities.interest_entity import Interest

class InterestRepository(ABC):

    @abstractmethod
    def create(self, interest: Interest) -> Interest:
        pass

    @abstractmethod
    def get_by_profile_id(self, profile_id: int) -> list[Interest]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Interest | None:
        pass
    
    @abstractmethod
    def get_all(self) -> list[Interest]:
        pass

    @abstractmethod
    def update(self, interest: Interest) -> Interest:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> None:
        pass