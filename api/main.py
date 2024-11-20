import os

from fastapi import FastAPI, status
from sqlmodel import Session, SQLModel, create_engine

from application.services.generic.user_service import UserService
from infrastructure.repositories.user_respository import UserRepository
from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto

app = FastAPI()

sqlite_file_name = "database.db"
connection_string = f"sqlite:///{sqlite_file_name}"

connection_string = os.environ.get("DATABASE_URL", connection_string)

engine = create_engine(connection_string)
SQLModel.metadata.create_all(engine)
session = Session(engine)

repository = UserRepository(session=session)

service = UserService(session=session, repository=repository)


@app.get("/user/{user_id}", response_model=UserDto)
def get_user(user_id: int) -> UserDto:
    entity = service.get_by_id(user_id)
    return entity


@app.get("/user/")
def get_all_users() -> list[UserDto]:
    return list(service.get_all())


@app.put("/user/{user_id}")
def update_user(user_id: int, user: UpdateUserDto):
    if user_id != user.id:
        # ! TODO: maybe some kind of error and middleware
        return {"error": "id in path and in body do not match"}

    service.update(user)


@app.post("/user/", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUserDto):
    service.create(user)
