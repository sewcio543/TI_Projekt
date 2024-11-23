from pydantic import BaseModel


class CommentDto(BaseModel):
    id: int | None
    content: str
    user_id: int
    post_id: int


class CreateCommentDto(BaseModel):
    content: str
    user_id: int
    post_id: int


class UpdateCommentDto(BaseModel):
    id: int | None
    content: str
