from abc import ABC, abstractmethod
from collections.abc import Iterable

from sqlalchemy.ext.asyncio import AsyncSession


class IRepository[T](ABC):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

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
