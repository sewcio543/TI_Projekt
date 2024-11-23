from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession

from application.mapping.mapping import GrudgeMapper
from application.services.interfaces.igrudge_service import IGrudgeService
from domain.contracts.igrudge_repository import IGrudgeRepository
from shared.dto.grudge_dto import CreateGrudgeDto, GrudgeDto


class GrudgeService(IGrudgeService):
    mapper = GrudgeMapper

    def __init__(self, session: AsyncSession, repository: IGrudgeRepository) -> None:
        self.session = session
        self.repository = repository

    async def get_by_id(self, id: int) -> GrudgeDto:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        return self.mapper.to_dto(entity)

    async def get_all(self) -> Iterable[GrudgeDto]:
        grudges = await self.repository.get_all()
        return map(self.mapper.to_dto, grudges)

    async def create(self, dto: CreateGrudgeDto) -> int:
        if dto is None:
            raise ValueError("Invalid entity")

        entity = self.mapper.to_entity(dto)

        await self.repository.insert(entity)
        await self.session.commit()

        if entity.id is None:
            raise ValueError("Entity not created")

        return entity.id

    async def delete(self, id: int) -> None:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        await self.repository.delete(entity)
        await self.session.commit()
