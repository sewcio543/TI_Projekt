from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession

from application.mapping.mapping import UserMapper
from application.services.interfaces.iuser_service import IUserService
from domain.contracts.iuser_repository import IUserRepository
from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto


class UserService(IUserService):
    mapper = UserMapper

    def __init__(self, session: AsyncSession, repository: IUserRepository) -> None:
        self.session = session
        self.repository = repository

    async def get_by_id(self, id: int) -> UserDto:
        if id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        return self.mapper.to_dto(entity)

    async def get_all(self) -> Iterable[UserDto]:
        entities = await self.repository.get_all()
        return map(self.mapper.to_dto, entities)

    async def create(self, dto: CreateUserDto) -> int:
        if dto is None:
            raise ValueError("Invalid entity")

        entity = self.mapper.to_entity(dto)

        await self.repository.insert(entity)
        await self.session.commit()

        if entity.id is None:
            raise ValueError("Entity not created")

        return entity.id

    async def update(self, dto: UpdateUserDto) -> UserDto:
        if dto is None:
            raise ValueError("Invalid entity")

        if dto.id is None or dto.id < 0:
            raise ValueError("Invalid id")

        entity = await self.repository.get(dto.id)

        if entity is None:
            raise ValueError("Entity not found")

        # ! TODO: smart way to update entity
        entity.login = dto.login
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
