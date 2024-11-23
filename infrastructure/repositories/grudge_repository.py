from collections.abc import Iterable

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from domain.contracts.igrudge_repository import IGrudgeRepository
from domain.models.db_models import Grudge
from infrastructure.repositories.repository import Repository


class GrudgeRepository(Repository[Grudge], IGrudgeRepository):
    model = Grudge

    async def exists(self, id: int) -> bool:
        entity = await self.session.get(self.model, id)
        return entity is not None

    async def get(self, id: int) -> Grudge:
        stmt = (
            select(Grudge)
            .options(joinedload(Grudge.user))  # type: ignore
            .options(joinedload(Grudge.post))  # type: ignore
            .filter_by(id=id)
        )
        result = await self.session.execute(stmt)
        post = result.scalars().one()
        return post

    async def get_all(self) -> Iterable[Grudge]:
        stmt = (
            select(Grudge)
            .options(joinedload(Grudge.user))  # type: ignore
            .options(joinedload(Grudge.post))  # type: ignore
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
