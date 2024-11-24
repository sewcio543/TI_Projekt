from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from sqlalchemy import text

import api.routers.comment_controller as comments
import api.routers.grudge_controller as grudges
import api.routers.post_controller as posts
import api.routers.user_controller as users
from api.authorization import JWTTokenHandler, Token
from api.helpers import Repositories, Services
from application.services.generic.comment_service import CommentService
from application.services.generic.grudge_service import GrudgeService
from application.services.generic.identity_service import IdentityService
from application.services.generic.post_service import PostService
from application.services.generic.user_service import UserService
from application.services.interfaces.iuser_service import IUserService
from connections.setup import get_connection
from infrastructure.repositories.comment_repository import CommentRepository
from infrastructure.repositories.grudge_repository import GrudgeRepository
from infrastructure.repositories.post_repository import PostRepository
from infrastructure.repositories.user_respository import UserRepository
from shared.dto.identity_dto import IdentityDto
from shared.dto.user_dto import UserDto

# from testing.helpers import seed_database

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "dbf4e8585c184da6494f6b3dc5d44ef18d1aa69657914e39ebf832bc37e03535"
ALGORITHM = "HS256"
TOKEN_DURATION = timedelta(minutes=15)

token_generator = JWTTokenHandler(secret=SECRET_KEY, algorithm=ALGORITHM)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


connection = get_connection()
session = connection.connect()

# _ = seed_database(session)

repositories = Repositories(
    users=UserRepository(session=session),
    posts=PostRepository(session=session),
    comments=CommentRepository(session=session),
    grudges=GrudgeRepository(session=session),
)

services = Services(
    users=UserService(
        session=session, repository=repositories.users, hasher=pwd_context
    ),
    posts=PostService(session=session, repository=repositories.posts),
    comments=CommentService(session=session, repository=repositories.comments),
    grudges=GrudgeService(session=session, repository=repositories.grudges),
    identity=IdentityService(repository=repositories.users, hasher=pwd_context),
)

user_controller = users.UserController(service=services.users)
post_controller = posts.PostController(service=services.posts)
comment_controller = comments.CommentController(service=services.comments)
grudge_controller = grudges.GrudgeController(service=services.grudges)

app.include_router(user_controller.router)
app.include_router(post_controller.router)
app.include_router(comment_controller.router)
app.include_router(grudge_controller.router)


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "oj bratku, działa"}


@app.get("/db_health", status_code=status.HTTP_200_OK)
async def db_health_check():
    async with session as sess:
        cursor = await sess.execute(text("SELECT version()"))
        return f"Ok {cursor.one()[0]}"


async def get_current_user_(
    token: Annotated[str, Depends(oauth2_scheme)],
    service: Annotated[IUserService, Depends(services.get_user_service)],
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


@app.get("/user/me/", response_model=UserDto)
async def get_current_user(user: Annotated[UserDto, Depends(get_current_user_)]):
    return user


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    dto = IdentityDto(login=form_data.username, password=form_data.password)
    user = await services.identity.authenticate(dto)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return token_generator.generate(user)
