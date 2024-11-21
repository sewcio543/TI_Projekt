from pydantic import BaseModel


class PostDto(BaseModel):
    id: int | None
    content: str | None
    user_id: int | None


class CreatePostDto(BaseModel):
    content: str | None
    user_id: int


class UpdatePostDto(BaseModel):
    id: int | None
    content: str | None
