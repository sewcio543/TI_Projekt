from fastapi import APIRouter, status

from application.services.interfaces.iuser_service import IUserService
from shared.dto import CreateUserDto, UpdateUserDto, UserDto


class UserController:
    router = APIRouter(prefix="/user", tags=["user"])

    def __init__(self, service: IUserService) -> None:
        self.service = service
        self.router = APIRouter(prefix="/user", tags=["user"])
        self.router.add_api_route(
            "/{user_id}", self.get, response_model=UserDto, methods=["GET"]
        )
        self.router.add_api_route(
            "/", self.get_alls, response_model=list[UserDto], methods=["GET"]
        )
        self.router.add_api_route("/{user_id}", self.update, methods=["PUT"])
        self.router.add_api_route(
            "/", self.create, status_code=status.HTTP_201_CREATED, methods=["POST"]
        )
        self.router.add_api_route(
            "/{user_id}",
            self.delete,
            status_code=status.HTTP_200_OK,
            methods=["DELETE"],
        )

    async def get(self, user_id: int) -> UserDto:
        entity = await self.service.get_by_id(user_id)
        return entity

    async def get_alls(self) -> list[UserDto]:
        users = await self.service.get_all()
        return list(users)

    async def update(self, user_id: int, user: UpdateUserDto):
        if user_id != user.id:
            # ! TODO: maybe some kind of error and middleware
            return {"error": "id in path and in body do not match"}

        return await self.service.update(user)

    async def create(self, user: CreateUserDto):
        user_id = await self.service.create(user)
        return {"id": user_id}

    async def delete(self, user_id: int):
        await self.service.delete(user_id)
        return {"msg": f"deleted user {user_id}"}
