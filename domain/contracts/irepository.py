from abc import ABC, abstractmethod
from collections.abc import Iterable


class IRepository[T](ABC):
    @abstractmethod
    async def get(self, id: int) -> T:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> Iterable[T]:
        raise NotImplementedError

    @abstractmethod
    async def insert(self, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, entity: T) -> None:
        raise NotImplementedError
