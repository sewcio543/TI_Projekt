from fastapi import FastAPI, status
from sqlalchemy import text

import api.routers.comment_controller as comments
import api.routers.grudge_controller as grudges
import api.routers.post_controller as posts
import api.routers.user_controller as users
from api.helpers import Repositories, Services
from application.services.generic.comment_service import CommentService
from application.services.generic.grudge_service import GrudgeService
from application.services.generic.post_service import PostService
from application.services.generic.user_service import UserService
from connections.setup import get_connection
from infrastructure.repositories.comment_repository import CommentRepository
from infrastructure.repositories.grudge_repository import GrudgeRepository
from infrastructure.repositories.post_repository import PostRepository
from infrastructure.repositories.user_respository import UserRepository

app = FastAPI()


connection = get_connection()
session = connection.connect()

repositories = Repositories(
    users=UserRepository(session=session),
    posts=PostRepository(session=session),
    comments=CommentRepository(session=session),
    grudges=GrudgeRepository(session=session),
)

services = Services(
    users=UserService(session=session, repository=repositories.users),
    posts=PostService(session=session, repository=repositories.posts),
    comments=CommentService(session=session, repository=repositories.comments),
    grudges=GrudgeService(session=session, repository=repositories.grudges),
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
