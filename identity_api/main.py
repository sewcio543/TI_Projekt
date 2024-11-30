from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

from api.authorization import JWTTokenHandler, Token
from application.services.generic.identity_service import IdentityService
from connections.setup import get_connection
from infrastructure.repositories.user_respository import UserRepository
from shared.dto.identity_dto import IdentityDto
from shared.dto.user_dto import UserDto

auth_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "dbf4e8585c184da6494f6b3dc5d44ef18d1aa69657914e39ebf832bc37e03535"
ALGORITHM = "HS256"
TOKEN_DURATION = timedelta(minutes=15)

token_generator = JWTTokenHandler(
    secret=SECRET_KEY,
    algorithm=ALGORITHM,
    duration=TOKEN_DURATION,
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

connection = get_connection()
session = connection.connect()

users_repository = UserRepository(session=session)
service = IdentityService(repository=users_repository, hasher=pwd_context)

app = FastAPI(title="GrudgeHub Identity API")

origins = ["http://localhost:3000", "http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SAME FUNCTIONALITY AS IN IDENTITY API, BUT JUST SENDING REQUESTS TO IDENTITY API


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
