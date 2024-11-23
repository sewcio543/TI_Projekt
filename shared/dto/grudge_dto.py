from pydantic import BaseModel


class GrudgeDto(BaseModel):
    id: int | None
    user_id: int
    post_id: int


class CreateGrudgeDto(BaseModel):
    user_id: int
    post_id: int
