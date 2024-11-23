from sqlalchemy.ext.asyncio import AsyncSession

from api.log import log
from domain.models.db_models import Comment, Grudge, Post, User


async def seed_database(session: AsyncSession) -> None:
    user1 = User(login="login1")
    user2 = User(login="login2")

    post1 = Post(content="content1", user=user1)
    post2 = Post(content="content2", user=user2)

    grudge1 = Grudge(post=post1, user=user1)
    grudge2 = Grudge(post=post1, user=user2)
    grudge3 = Grudge(post=post2, user=user2)

    comment1 = Comment(content="Excellent", user=user1, post=post1)
    comment2 = Comment(content="It sucks dude!", user=user2, post=post1)
    comment3 = Comment(content="I agree", user=user1, post=post2)

    entities = [
        user1,
        user2,
        post1,
        post2,
        grudge1,
        grudge2,
        grudge3,
        comment1,
        comment2,
        comment3,
    ]
    session.add_all(entities)
    _ = session.commit()
    log.info("Database seeded with mock data")
