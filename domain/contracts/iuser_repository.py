from typing import Iterable

from domain.contracts.irepository import IRepository
from domain.models.db_models import User


class IUserRepository(IRepository[User]):
    def get(self, id: int) -> User:
        raise NotImplementedError

    def get_all(self) -> Iterable[User]:
        raise NotImplementedError

    def exists(self, id: int) -> bool:
        raise NotImplementedError
