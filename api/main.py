import os

from fastapi import FastAPI, status
from sqlmodel import Session, SQLModel, create_engine

from application.services.generic.user_service import UserService
from infrastructure.repositories.user_respository import UserRepository
from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto

from api.helpers import get_db_url_from_env, init_postgres_ctx
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

app = FastAPI()


db_url = get_db_url_from_env()
async_session = init_postgres_ctx(db_url)()

repository = UserRepository(session=async_session)
service = UserService(session=async_session, repository=repository)


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "oj bratku, działa"}


@app.get("/db_health", status_code=status.HTTP_200_OK)
async def db_health_check():
    async with async_session as sess:
        cursor = await sess.execute(text("SELECT version()"))
        return f"Ok {cursor.one()[0]}"
                    

@app.get("/user/{user_id}", response_model=UserDto)
async def get_user(user_id: int) -> UserDto:
    entity = await service.get_by_id(user_id)
    return entity


@app.get("/user/")
async def get_all_users() -> list[UserDto]:
    users = await service.get_all()
    return list(users)


@app.put("/user/{user_id}")
async def update_user(user_id: int, user: UpdateUserDto):
    if user_id != user.id:
        # ! TODO: maybe some kind of error and middleware
        return {"error": "id in path and in body do not match"}

    return await service.update(user)


@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserDto):
    user_id = await service.create(user)
    return {"id": user_id}
    
