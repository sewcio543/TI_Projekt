from pydantic import BaseModel


class UserDto(BaseModel):
    id: int | None
    login: str


class CreateUserDto(BaseModel):
    login: str


class UpdateUserDto(BaseModel):
    id: int | None
    login: str
