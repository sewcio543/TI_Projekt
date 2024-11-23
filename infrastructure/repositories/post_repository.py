from collections.abc import Iterable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from domain.contracts.ipost_repository import IPostRepository
from domain.models.db_models import Post
from infrastructure.repositories.repository import Repository


class PostRepository(Repository[Post], IPostRepository):
    model = Post

    def __init__(self, session: AsyncSession):
        self.session = session

    async def exists(self, id: int) -> bool:
        entity = await self.session.get(self.model, id)
        return entity is not None

    async def get(self, id: int) -> Post:
        stmt = select(Post).options(joinedload(Post.user)).filter_by(id=id)  # type: ignore
        result = await self.session.execute(stmt)
        post = result.scalars().one()
        return post

    async def get_all(self) -> Iterable[Post]:
        stmt = select(Post).options(joinedload(Post.user))  # type: ignore
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
