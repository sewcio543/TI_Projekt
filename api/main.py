from fastapi import FastAPI, status
from sqlmodel import Session, SQLModel, create_engine

from application.services.generic.user_service import UserService
from infrastructure.repositories.user_respository import UserRepository
from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto

app = FastAPI()

sqlite_file_name = "databases.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)
SQLModel.metadata.create_all(engine)
session = Session(engine)

repository = UserRepository(session=session)

service = UserService(session=session, repository=repository)


@app.get("/user/{id}")
def get_user(user_id: int) -> UserDto:
    entity = service.get_by_id(user_id)
    return entity


@app.get("/users/")
def get_all_users() -> list[UserDto]:
    return list(service.get_all())


@app.put("/user/{id}")
def update_user(user_id: int, user: UpdateUserDto):
    if user_id != user.id:
        # ! TODO: maybe some kind of error and middleware
        return {"error": "id in path and in body do not match"}

    service.update(user)


@app.post("/user/", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUserDto):
    service.create(user)
