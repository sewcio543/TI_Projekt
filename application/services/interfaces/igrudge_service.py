from abc import ABC, abstractmethod
from typing import Iterable

from shared.dto.grudge_dto import CreateGrudgeDto, GrudgeDto


class IGrudgeService(ABC):
    @abstractmethod
    async def get_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> Iterable[GrudgeDto]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, dto: CreateGrudgeDto) -> int:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int) -> None:
        raise NotImplementedError
