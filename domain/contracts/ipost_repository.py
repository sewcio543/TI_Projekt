from typing import Iterable

from domain.contracts.irepository import IRepository
from domain.models.db_models import Post


class IPostRepository(IRepository[Post]):
    async def get(self, id: int) -> Post:
        raise NotImplementedError

    async def get_all(self) -> Iterable[Post]:
        raise NotImplementedError

    async def exists(self, id: int) -> bool:
        raise NotImplementedError
