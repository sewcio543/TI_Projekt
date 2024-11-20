from abc import ABC, abstractmethod
from collections.abc import Iterable


class IRepository[T](ABC):
    @abstractmethod
    def get(self, id: int) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Iterable[T]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity: T) -> None:
        raise NotImplementedError
