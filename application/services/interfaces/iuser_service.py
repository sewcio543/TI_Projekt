from abc import ABC, abstractmethod
from collections.abc import Iterable

from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto

# ? Do we want to make some DTOs?


class IUserService(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> UserDto:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Iterable[UserDto]:
        raise NotImplementedError

    @abstractmethod
    def create(self, dto: CreateUserDto) -> int:
        raise NotImplementedError

    @abstractmethod
    def update(self, dto: UpdateUserDto) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError
