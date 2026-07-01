from app.core.exceptions.user_exception import UserNotFoundException
from app.domain.repositories.profile_repository import ProfileRepository
from app.domain.repositories.user_repository import UserRepository
from app.schemas.user.profile_schema import ProfileResponse
from app.schemas.user.user_schema import UserWithProfileResponse


class UserService:

    def __init__(
        self,
        user_repository: UserRepository,
        profile_repository: ProfileRepository,
    ):
        self.user_repository = user_repository
        self.profile_repository = profile_repository

    def me(self, user_id: int) -> UserWithProfileResponse:
        user = self.user_repository.get_by_id(user_id)

        if user is None:
            raise UserNotFoundException()

        profile = self.profile_repository.get_by_user_id(user_id)

        return UserWithProfileResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            profile=(
                ProfileResponse.model_validate(profile)
                if profile
                else None
            ),
        )