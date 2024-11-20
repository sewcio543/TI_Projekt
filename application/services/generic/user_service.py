from typing import Iterable

from sqlmodel import Session

from application.mapping.mapping import dto_to_user, user_to_dto
from application.services.interfaces.iuser_service import IUserService
from domain.contracts.iuser_repository import IUserRepository
from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto


class UserService(IUserService):
    def __init__(self, session: Session, repository: IUserRepository) -> None:
        self.session = session
        self.repository = repository

    def get_by_id(self, id: int) -> UserDto:
        if id < 0:
            raise ValueError("Invalid id")

        entity = self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        return user_to_dto(entity)

    def get_all(self) -> Iterable[UserDto]:
        return map(user_to_dto, self.repository.get_all())

    def create(self, dto: CreateUserDto) -> int:
        if dto is None:
            raise ValueError("Invalid entity")

        user = dto_to_user(dto)

        self.repository.insert(user)
        self.session.commit()

        if user.id is None:
            raise ValueError("Entity not created")

        return user.id

    def update(self, dto: UpdateUserDto) -> None:
        if dto is None:
            raise ValueError("Invalid entity")

        if dto.id is None or dto.id < 0:
            raise ValueError("Invalid id")

        entity_ = self.repository.get(dto.id)

        if entity_ is None:
            raise ValueError("Entity not found")

        # ! TODO: smart way to update entity
        entity_.login = dto.login

        self.session.commit()

    def delete(self, id: int) -> None:
        if id < 0:
            raise ValueError("Invalid id")

        entity = self.repository.get(id)

        if entity is None:
            raise ValueError("Entity not found")

        self.repository.delete(entity)
        self.session.commit()
