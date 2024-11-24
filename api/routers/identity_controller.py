from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError

from api.authorization import Token
from api.dependencies import dep
from shared.dto.identity_dto import IdentityDto
from shared.dto.user_dto import UserDto

router = APIRouter(tags=["identity"])


async def verify_user(
    token: Annotated[str, Depends(dep.auth_scheme)],
) -> UserDto:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        token_data = dep.token_generator.decode(token)
        if token_data.login is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    user = await dep.services.users.get_by_login(token_data.login)

    if user is None:
        raise credentials_exception

    return user


Authorization = Annotated[UserDto, Depends(verify_user)]


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    dto = IdentityDto(login=form_data.username, password=form_data.password)
    user = await dep.services.identity.authenticate(dto)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return dep.token_generator.generate(user)
