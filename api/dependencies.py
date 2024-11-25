from dataclasses import dataclass
from datetime import timedelta
from typing import Any

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from api.authorization import JWTTokenHandler
from api.helpers import Repositories, Services
from application.services.generic.comment_service import CommentService
from application.services.generic.grudge_service import GrudgeService
from application.services.generic.identity_service import IdentityService
from application.services.generic.post_service import PostService
from application.services.generic.user_service import UserService
from connections.setup import get_connection
from infrastructure.repositories.comment_repository import CommentRepository
from infrastructure.repositories.grudge_repository import GrudgeRepository
from infrastructure.repositories.post_repository import PostRepository
from infrastructure.repositories.user_respository import UserRepository
from application.sentiment.moderator import Moderator
from application.sentiment.textblob_analyzer import TextBlobAnalyzer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

moderator = Moderator(analyzer=TextBlobAnalyzer)

@dataclass
class Dependencies:
    services: Services
    repositories: Repositories
    token_generator: JWTTokenHandler
    auth_scheme: OAuth2PasswordBearer
    pwd_context: CryptContext
    session: AsyncSession
    moderator: Moderator

    def get(self, o: Any) -> Any:
        """Use as a dependency injection in FastAPI."""
        return o


dep = Dependencies(
    services=services,
    repositories=repositories,
    token_generator=token_generator,
    auth_scheme=oauth2_scheme,
    pwd_context=pwd_context,
    session=session,
    moderator=moderator
)
