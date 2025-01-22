from typing import Iterable

from domain.contracts.irepository import IRepository
from domain.models.db_models import Comment


class ICommentRepository(IRepository[Comment]):
    async def get(self, id: int) -> Comment:
        raise NotImplementedError

    async def get_by_post_id(self, post_id: int) -> Iterable[Comment]:
        raise NotImplementedError

    async def get_all(self) -> Iterable[Comment]:
        raise NotImplementedError

    async def exists(self, id: int) -> bool:
        raise NotImplementedError
