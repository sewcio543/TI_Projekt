from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession

from application.mapping.mapping import PostMapper
from application.services.interfaces.ipost_service import IPostService
from domain.contracts.ipost_repository import IPostRepository
from shared.dto.post_dto import CreatePostDto, PostDto, UpdatePostDto


class PostService(IPostService):
    mapper = PostMapper

    def __init__(self, session: AsyncSession, repository: IPostRepository) -> None:
        self.session = session
        self.repository = repository

    async def get_by_id(self, id: int) -> PostDto:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        return self.mapper.to_dto(entity)

    async def get_all(self) -> Iterable[PostDto]:
        entities = await self.repository.get_all()
        return map(self.mapper.to_dto, entities)

    async def create(self, dto: CreatePostDto) -> int:
        if dto is None:
            raise ValueError("Invalid entity")

        entity = self.mapper.to_entity(dto)

        await self.repository.insert(entity)
        await self.session.commit()

        if entity.id is None:
            raise ValueError("Entity not created")

        return entity.id

    async def update(self, dto: UpdatePostDto) -> PostDto:
        if dto is None:
            raise ValueError("Invalid entity")

        if dto.id is None or dto.id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(dto.id)

        if entity is None:
            raise ValueError("Entity not found")

        # ! TODO: smart way to update entity
        entity.content = dto.content
        await self.session.commit()

        return self.mapper.to_dto(entity)

    async def delete(self, id: int) -> None:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        await self.repository.delete(entity)
        await self.session.commit()
