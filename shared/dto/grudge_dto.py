from pydantic import BaseModel

from shared.dto.post_dto import PostDto
from shared.dto.user_dto import UserDto


class GrudgeDto(BaseModel):
    id: int | None
    user: UserDto
    post: PostDto


class CreateGrudgeDto(BaseModel):
    user: UserDto
    post: PostDto
