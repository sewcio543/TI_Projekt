from collections.abc import Iterable

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from domain.contracts.icomment_repository import ICommentRepository
from domain.models.db_models import Comment
from infrastructure.repositories.repository import Repository


class CommentRepository(Repository[Comment], ICommentRepository):
    model = Comment

    async def exists(self, id: int) -> bool:
        entity = await self.session.get(self.model, id)
        return entity is not None

    async def get(self, id: int) -> Comment:
        stmt = (
            select(Comment)
            .options(joinedload(Comment.user))  # type: ignore
            .options(joinedload(Comment.post))  # type: ignore
            .filter_by(id=id)
        )
        result = await self.session.execute(stmt)
        post = result.scalars().one()
        return post

    async def get_by_post_id(self, post_id: int) -> Iterable[Comment]:
        stmt = (
            select(Comment)
            .options(joinedload(Comment.user))  # type: ignore
            .options(joinedload(Comment.post))  # type: ignore
            .filter_by(post_id=post_id)
        )
        result = await self.session.execute(stmt)
        comment = result.scalars().all()
        return comment

    async def get_all(self) -> Iterable[Comment]:
        stmt = (
            select(Comment)
            .options(joinedload(Comment.user))  # type: ignore
            .options(joinedload(Comment.post))  # type: ignore
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
