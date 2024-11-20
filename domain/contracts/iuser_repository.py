from typing import Iterable

from domain.contracts.irepository import IRepository
from domain.models.db_models import User


class IUserRepository(IRepository[User]):
    async def get(self, id: int) -> User:
        raise NotImplementedError

    async def get_all(self) -> Iterable[User]:
        raise NotImplementedError

    async def exists(self, id: int) -> bool:
        raise NotImplementedError
