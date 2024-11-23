from abc import ABC, abstractmethod
from typing import Iterable

from shared.dto.comment_dto import CommentDto, CreateCommentDto, UpdateCommentDto


class ICommentService(ABC):
    @abstractmethod
    async def get_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> Iterable[CommentDto]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, dto: CreateCommentDto) -> int:
        raise NotImplementedError

    @abstractmethod
    async def update(self, dto: UpdateCommentDto) -> CommentDto:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int) -> None:
        raise NotImplementedError
