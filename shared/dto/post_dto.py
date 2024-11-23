from pydantic import BaseModel


class PostDto(BaseModel):
    id: int | None
    content: str
    user_id: int


class CreatePostDto(BaseModel):
    content: str
    user_id: int


class UpdatePostDto(BaseModel):
    id: int | None
    content: str
