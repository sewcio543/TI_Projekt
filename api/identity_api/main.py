from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError

from api import settings
from api.dependencies import dep
from api.shared.authorization import Token
from api.shared.cors import add_cors_middleware
from shared.dto.identity_dto import IdentityDto
from shared.dto.user_dto import UserDto

auth_scheme = OAuth2PasswordBearer(tokenUrl="token")

token_generator = dep.token_generator
pwd_context = dep.pwd_context
service = dep.services.identity

app = FastAPI(title="GrudgeHub Identity API")
add_cors_middleware(
    app,
    origins=[
        settings.FRONTEND_URL,
        settings.PEOPLE_API_URL,
        settings.CONTENT_API_URL,
    ],
)


@app.get("/verify", response_model=UserDto)
async def verify_user(
    token: Annotated[str, Depends(auth_scheme)],
) -> UserDto:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        token_data = token_generator.decode(token)

        if token_data.login is None:
            raise credentials_exception

    except InvalidTokenError:
        raise credentials_exception

    user = await service.get_by_login(token_data.login)

    if user is None:
        raise credentials_exception

    return user


Authorization = Annotated[UserDto, Depends(verify_user)]


@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    dto = IdentityDto(login=form_data.username, password=form_data.password)
    user = await service.authenticate(dto)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return token_generator.generate(user)
