from pydantic import BaseModel

from shared.dto.post_dto import PostDto
from shared.dto.user_dto import UserDto


class CommentDto(BaseModel):
    id: int | None
    content: str
    user: UserDto
    post: PostDto


class CreateCommentDto(BaseModel):
    content: str
    user_id: int
    post_id: int


class UpdateCommentDto(BaseModel):
    id: int | None
    content: str
