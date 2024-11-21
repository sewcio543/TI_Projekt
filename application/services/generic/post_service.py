from typing import Iterable

from sqlmodel import Session

from application.mapping.mapping import post_to_dto, dto_to_post
from application.services.interfaces.ipost_service import IPostService
from domain.contracts.ipost_repository import IPostRepository
from shared.dto.post_dto import CreatePostDto, UpdatePostDto, PostDto


class PostService(IPostService):
    def __init__(self, session: Session, repository: IPostRepository) -> None:
        self.session = session
        self.repository = repository

    async def get_by_id(self, id: int) -> PostDto:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        return post_to_dto(entity)

    async def get_all(self) -> Iterable[PostDto]:
        posts = await self.repository.get_all()
        return map(post_to_dto, posts)

    async def create(self, dto: CreatePostDto) -> int:
        if dto is None:
            raise ValueError("Invalid entity")

        post = dto_to_post(dto)

        await self.repository.insert(post)
        await self.session.commit()

        if post.id is None:
            raise ValueError("Entity not created")

        return post.id

    async def update(self, dto: UpdatePostDto) -> None:
        if dto is None:
            raise ValueError("Invalid entity")

        if dto.id is None or dto.id < 0:
            raise ValueError("Invalid id")

        entity_ = await self.repository.get(dto.id)

        if entity_ is None:
            raise ValueError("Entity not found")

        # ! TODO: smart way to update entity
        entity_.content = dto.content
        await self.session.commit()
        
        return post_to_dto(entity_)

    async def delete(self, id: int) -> None:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        await self.repository.delete(entity)
        await self.session.commit()
