from __future__ import annotations

from typing import List
from sqlmodel import Field, Relationship, SQLModel

class Base(SQLModel):
    ...


class User(Base, table=True):
    id: int | None = Field(default=None, primary_key=True)
    login: str

    posts: List[Post] = Relationship(back_populates="user")
#     comments: list[Comment] = Relationship(back_populates="user")


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str

    user_id: int | None = Field(default=None, foreign_key="user.id")
    user: User | None = Relationship(back_populates="posts")

#     comments: list[Comment] = Relationship(back_populates="post")


# class Comment(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     content: str

#     post_id: int | None = Field(default=None, foreign_key="post.id")
#     post: Post | None = Relationship(back_populates="comments")

#     user_id: int | None = Field(default=None, foreign_key="user.id")
#     user: User | None = Relationship(back_populates="comments")
