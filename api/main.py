import os

from fastapi import FastAPI, status
from sqlmodel import Session, SQLModel, create_engine

from application.services.generic.user_service import UserService
from application.services.generic.post_service import PostService
from infrastructure.repositories.user_respository import UserRepository
from infrastructure.repositories.post_repository import PostRepository
from shared.dto import (
    CreateUserDto,
    UpdateUserDto,
    UserDto,
    CreatePostDto,
    UpdatePostDto,
    PostDto,
)

from api.helpers import get_db_url_from_env, init_postgres_ctx
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

app = FastAPI()


db_url = get_db_url_from_env()
async_session = init_postgres_ctx(db_url)()

# todo make those into classes
repositories = {
    "user": UserRepository(session=async_session),
    "post": PostRepository(session=async_session),
}
services = {
    "user": UserService(session=async_session, repository=repositories['user']),
    "post": PostService(session=async_session, repository=repositories['post']),
}



@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "oj bratku, działa"}


@app.get("/db_health", status_code=status.HTTP_200_OK)
async def db_health_check():
    async with async_session as sess:
        cursor = await sess.execute(text("SELECT version()"))
        return f"Ok {cursor.one()[0]}"
    
""" USER CRUD """                

@app.get("/user/{user_id}", response_model=UserDto)
async def get_user(user_id: int) -> UserDto:
    entity = await services['user'].get_by_id(user_id)
    return entity


@app.get("/user/")
async def get_all_users() -> list[UserDto]:
    users = await services['user'].get_all()
    return list(users)


@app.put("/user/{user_id}")
async def update_user(user_id: int, user: UpdateUserDto):
    if user_id != user.id:
        # ! TODO: maybe some kind of error and middleware
        return {"error": "id in path and in body do not match"}

    return await services['user'].update(user)


@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserDto):
    user_id = await services['user'].create(user)
    return {"id": user_id}

@app.delete("/user/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int):
    await services['user'].delete(user_id)
    return {"msg": f"deleted user {user_id}"}

    
""" POSTS CRUD """
@app.get("/post/{post_id}", response_model=PostDto)
async def get_post(post_id: int) -> PostDto:
    entity = await services['post'].get_by_id(post_id)
    return entity


@app.get("/post/")
async def get_all_posts() -> list[PostDto]:
    posts = await services['post'].get_all()
    
    return list(posts)


@app.put("/post/{post_id}")
async def update_post(post_id: int, post: UpdatePostDto):
    if post_id != post.id:
        # ! TODO: maybe some kind of error and middleware
        return {"error": "id in path and in body do not match"}

    return await services['post'].update(post)


@app.post("/post/", status_code=status.HTTP_201_CREATED)
async def create_post(post: CreatePostDto):
    post_id = await services['post'].create(post)
    return {"id": post_id}

@app.delete("/post/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int):
    await services['post'].delete(post_id)
    return {"msg": f"deleted post {post_id}"}
                
