from abc import ABC, abstractmethod
from typing import Iterable
from shared.dto.post_dto import CreatePostDto, UpdatePostDto, PostDto



class IPostService(ABC):
    @abstractmethod
    def get_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Iterable[PostDto]:
        raise NotImplementedError

    @abstractmethod
    def create(self, dto: CreatePostDto) -> int:
        raise NotImplementedError

    @abstractmethod
    def update(self, dto: UpdatePostDto) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError