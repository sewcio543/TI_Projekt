from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession

from application.mapping.mapping import dto_to_post, post_to_dto
from application.services.interfaces.ipost_service import IPostService
from domain.contracts.ipost_repository import IPostRepository
from shared.dto.post_dto import CreatePostDto, PostDto, UpdatePostDto


class PostService(IPostService):
    def __init__(self, session: AsyncSession, repository: IPostRepository) -> None:
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

    async def update(self, dto: UpdatePostDto) -> PostDto:
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
