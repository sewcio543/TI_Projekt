from sqlalchemy import select

from domain.contracts.iuser_repository import IUserRepository
from domain.models.db_models import User
from infrastructure.repositories.repository import Repository


class UserRepository(Repository[User], IUserRepository):
    model = User

    async def exists(self, login: str) -> bool:
        condition = User.login == login
        stmt = select(User).where(condition)  # type: ignore
        result = await self.session.execute(stmt)
        return result.first() is not None

    async def get_by_login(self, login: str) -> User | None:
        condition = User.login == login
        stmt = select(User).where(condition)  # type: ignore
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
