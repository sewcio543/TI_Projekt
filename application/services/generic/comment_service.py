from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession

from application.mapping.mapping import CommentMapper
from application.services.interfaces.icomment_service import ICommentService
from domain.contracts.icomment_repository import ICommentRepository
from shared.dto.comment_dto import CommentDto, CreateCommentDto, UpdateCommentDto


class CommentService(ICommentService):
    mapper = CommentMapper

    def __init__(self, session: AsyncSession, repository: ICommentRepository) -> None:
        self.session = session
        self.repository = repository

    async def get_by_id(self, id: int) -> CommentDto:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        return self.mapper.to_dto(entity)

    async def get_all(self) -> Iterable[CommentDto]:
        entities = await self.repository.get_all()
        return map(self.mapper.to_dto, entities)

    async def create(self, dto: CreateCommentDto) -> int:
        if dto is None:
            raise ValueError("Invalid entity")

        entity = self.mapper.to_entity(dto)

        await self.repository.insert(entity)
        await self.session.commit()

        if entity.id is None:
            raise ValueError("Entity not created")

        return entity.id

    async def update(self, dto: UpdateCommentDto) -> CommentDto:
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

        return self.mapper.to_dto(entity_)

    async def delete(self, id: int) -> None:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        await self.repository.delete(entity)
        await self.session.commit()
