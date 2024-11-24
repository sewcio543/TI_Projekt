from abc import ABC, abstractmethod
from collections.abc import Iterable

from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto


class IUserService(ABC):
    @abstractmethod
    async def get_by_id(self, id: int) -> UserDto:
        raise NotImplementedError

    @abstractmethod
    async def get_by_login(self, login: str) -> UserDto:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> Iterable[UserDto]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, dto: CreateUserDto) -> int:
        raise NotImplementedError

    @abstractmethod
    async def update(self, dto: UpdateUserDto) -> UserDto:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int) -> None:
        raise NotImplementedError
