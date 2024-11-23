from abc import ABC, abstractmethod
from typing import Any


class DtoMapper[T](ABC):

    @classmethod
    @abstractmethod
    def to_dto(cls, entity: T) -> Any:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def to_entity(cls, dto: Any) -> T:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def update(cls, entity: T, dto: Any) -> T:
        raise NotImplementedError
