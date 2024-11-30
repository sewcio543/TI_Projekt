from datetime import datetime, timedelta, timezone
from typing import Annotated, Protocol

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from httpx import AsyncClient
from pydantic import BaseModel, ValidationError

from shared.dto import UserDto
from shared.dto.identity_dto import IdentityDto
from shared.dto.user_dto import UserDto

router = APIRouter(tags=["authentication"])

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


client = AsyncClient()
auth_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def verify_user(
    token: Annotated[str, Depends(auth_scheme)],
) -> UserDto:
    headers = {"Authorization": f"Bearer {token}"}
    response = await client.get("http://localhost:8000/verify", headers=headers)

    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    user_json = response.json()

    try:
        user = UserDto(**user_json)
    except ValidationError as e:
        #! TODO - extract error message from pydantic
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        ) from e

    return user


Authorization = Annotated[UserDto, Depends(verify_user)]


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    data = {"username": form_data.username, "password": form_data.password}

    response = await client.post("http://localhost:8000/token", data=data)

    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token_json = response.json()

    try:
        token = Token(**token_json)
    except ValidationError as e:
        #! TODO - extract error message from pydantic
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        ) from e

    return token
