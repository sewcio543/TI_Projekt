import logging
from typing import Annotated

import httpx
import pydantic
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from api import settings
from api.shared.token_handler import Token
from shared.dto import UserDto
from shared.dto.user_dto import UserDto

auth_scheme = OAuth2PasswordBearer(tokenUrl=settings.TOKEN_URL)


async def verify_user(
    token: Annotated[str, Depends(auth_scheme)],
) -> UserDto:
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(
                #! TODO: idk why, but localhost does not work for /verify
                #! it works for /token though wtf
                "http://identity_api:8000/verify",
                headers=headers,
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            logging.error(f"HTTPStatusError: {exc.response.text}")
            raise HTTPException(
                status_code=exc.response.status_code,
                detail=f"Error verifying token: {exc.response.text}",
            )
        except httpx.RequestError as exc:
            logging.error(f"RequestError: {exc}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error connecting to identity service: {exc}",
            )

    user_json = response.json()
    logging.info(f"Received response: {user_json}")

    try:
        user = UserDto(**user_json)
    except pydantic.ValidationError as e:
        logging.error(f"ValidationError: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error parsing user data",
        ) from e

    return user


Authorization = Annotated[UserDto, Depends(verify_user)]


async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    data = {"username": form_data.username, "password": form_data.password}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(settings.TOKEN_URL, data=data)
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(
                status_code=exc.response.status_code,
                detail=f"Invalid credentials: {exc.response.text}",
            )
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error connecting to identity service: {exc}",
            )

    token_json = response.json()

    try:
        token = Token(**token_json)
    except pydantic.ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error parsing user data",
        ) from e

    return token
