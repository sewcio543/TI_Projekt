from pydantic import BaseModel

from shared.dto.user_dto import UserDto


class PostDto(BaseModel):
    id: int | None
    content: str
    user: UserDto


class CreatePostDto(BaseModel):
    content: str
    user: UserDto


class UpdatePostDto(BaseModel):
    id: int | None
    content: str
