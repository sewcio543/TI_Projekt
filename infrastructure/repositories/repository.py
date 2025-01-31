from collections.abc import Iterable

from sqlmodel import SQLModel, select

from domain.contracts.irepository import IRepository


class Repository[T](IRepository[T]):
    model: type[SQLModel]

    async def get(self, id: int) -> T:
        return await self.session.get(self.model, id)  # type: ignore

    async def get_all(self) -> Iterable[T]:
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())  # type: ignore

    async def insert(self, entity: T) -> None:
        self.session.add(entity)

    async def delete(self, entity: T) -> None:
        await self.session.delete(entity)
