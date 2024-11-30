from abc import ABC, abstractmethod
from collections.abc import Iterable

from shared.dto.identity_dto import IdentityDto
from shared.dto.user_dto import UserDto


class IIdentityService(ABC):
    @abstractmethod
    async def authenticate(self, dto: IdentityDto) -> UserDto | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_login(self, login: str) -> UserDto:
        raise NotImplementedError
