from pydantic import BaseModel


class IdentityDto(BaseModel):
    login: str
    password: str
