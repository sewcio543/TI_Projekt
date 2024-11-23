from typing import Iterable

from domain.contracts.irepository import IRepository
from domain.models.db_models import Grudge


class IGrudgeRepository(IRepository[Grudge]):
    async def get(self, id: int) -> Grudge:
        raise NotImplementedError

    async def get_all(self) -> Iterable[Grudge]:
        raise NotImplementedError

    async def exists(self, id: int) -> bool:
        raise NotImplementedError
