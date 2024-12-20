from datetime import datetime, timedelta, timezone
from typing import Protocol

import jwt
from pydantic import BaseModel

from shared.dto import UserDto
from shared.dto.user_dto import UserDto

SUB_KEY = "sub"
EXP_KEY = "exp"


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    login: str | None = None

    def is_valid(self) -> bool:
        return self.login is not None


class ITokenHandler(Protocol):
    def generate(self, data: UserDto) -> Token:
        raise NotImplementedError

    def decode(self, token: str) -> TokenData:
        raise NotImplementedError


DEFAULT_DURATION = timedelta(minutes=15)
DEFAULT_ALGORITHM = "HS256"


class JWTTokenHandler(ITokenHandler):
    def __init__(
        self,
        secret: str,
        algorithm: str = DEFAULT_ALGORITHM,
        duration: timedelta | None = None,
    ) -> None:
        self._key = secret
        self._algorithm = algorithm
        self._duration = duration or DEFAULT_DURATION

    def generate(self, dto: UserDto) -> Token:
        expire = datetime.now(timezone.utc) + self._duration
        to_encode = {SUB_KEY: dto.login, EXP_KEY: expire}
        token = jwt.encode(to_encode, key=self._key, algorithm=self._algorithm)
        return Token(access_token=token, token_type="bearer")

    def decode(self, token: str) -> TokenData:
        payload: dict = jwt.decode(token, key=self._key, algorithms=[self._algorithm])
        login = payload.get(SUB_KEY)
        return TokenData(login=login)
