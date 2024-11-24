from application.services.interfaces.iidentity_service import IIdentityService
from application.services.password_services import IHashingContext
from domain.contracts.iuser_repository import IUserRepository
from shared.dto.identity_dto import IdentityDto
from shared.dto.user_dto import UserDto


class IdentityService(IIdentityService):
    def __init__(self, repository: IUserRepository, hasher: IHashingContext) -> None:
        self.repository = repository
        self.hasher = hasher

    async def authenticate(self, dto: IdentityDto) -> UserDto | None:
        if dto is None:
            raise ValueError("Invalid entity")

        user = await self.repository.get_by_login(dto.login)

        if user is None:
            return None

        valid = self.hasher.verify(secret=dto.password, hash=user.hashed_password)

        if not valid:
            return None

        return UserDto(id=user.id, login=user.login)
