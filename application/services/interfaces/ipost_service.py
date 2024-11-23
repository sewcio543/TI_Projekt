from abc import ABC, abstractmethod
from typing import Iterable

from shared.dto.post_dto import CreatePostDto, PostDto, UpdatePostDto


class IPostService(ABC):
    @abstractmethod
    async def get_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> Iterable[PostDto]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, dto: CreatePostDto) -> int:
        raise NotImplementedError

    @abstractmethod
    async def update(self, dto: UpdatePostDto) -> PostDto:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int) -> None:
        raise NotImplementedError
