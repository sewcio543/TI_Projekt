from pydantic import BaseModel


class UserDto(BaseModel):
    id: int | None
    login: str


class CreateUserDto(BaseModel):
    login: str
    password: str


class UpdateUserDto(BaseModel):
    id: int | None
    login: str
    password: str


class DBUserDto(BaseModel):
    id: int
    login: str
    hashed_password: str
