from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession

from application.mapping.mapping import comment_to_dto, dto_to_comment
from application.services.interfaces.icomment_service import ICommentService
from domain.contracts.icomment_repository import ICommentRepository
from shared.dto.comment_dto import CommentDto, CreateCommentDto, UpdateCommentDto


class CommentService(ICommentService):
    def __init__(self, session: AsyncSession, repository: ICommentRepository) -> None:
        self.session = session
        self.repository = repository

    async def get_by_id(self, id: int) -> CommentDto:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        return comment_to_dto(entity)

    async def get_all(self) -> Iterable[CommentDto]:
        Comments = await self.repository.get_all()
        return map(comment_to_dto, Comments)

    async def create(self, dto: CreateCommentDto) -> int:
        if dto is None:
            raise ValueError("Invalid entity")

        Comment = dto_to_comment(dto)

        await self.repository.insert(Comment)
        await self.session.commit()

        if Comment.id is None:
            raise ValueError("Entity not created")

        return Comment.id

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

        return comment_to_dto(entity_)

    async def delete(self, id: int) -> None:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        await self.repository.delete(entity)
        await self.session.commit()
