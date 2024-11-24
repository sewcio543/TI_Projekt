from sqlmodel import Field, Relationship, SQLModel


class Base(SQLModel): ...


class User(Base, table=True):
    id: int | None = Field(default=None, primary_key=True)
    login: str
    hashed_password: str

    posts: list["Post"] = Relationship(back_populates="user")
    comments: list["Comment"] = Relationship(back_populates="user")
    grudges: list["Grudge"] = Relationship(back_populates="user")


class Post(Base, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str

    user_id: int = Field(default=None, foreign_key="user.id")
    user: User = Relationship(back_populates="posts")

    comments: list["Comment"] = Relationship(back_populates="post")
    grudges: list["Grudge"] = Relationship(back_populates="post")


class Comment(Base, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str

    post_id: int = Field(default=None, foreign_key="post.id")
    post: Post = Relationship(back_populates="comments")

    user_id: int = Field(default=None, foreign_key="user.id")
    user: User = Relationship(back_populates="comments")


class Grudge(Base, table=True):
    id: int | None = Field(default=None, primary_key=True)

    post_id: int = Field(default=None, foreign_key="post.id")
    post: Post = Relationship(back_populates="grudges")

    user_id: int = Field(default=None, foreign_key="user.id")
    user: User = Relationship(back_populates="grudges")
