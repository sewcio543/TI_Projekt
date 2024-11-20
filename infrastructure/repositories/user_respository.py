from domain.contracts.iuser_repository import IUserRepository
from domain.models.db_models import User
from infrastructure.repositories.repository import Repository


class UserRepository(Repository[User], IUserRepository):
    model = User

    def exists(self, id: int) -> bool:
        entity = self.session.get(self.model, id)
        return entity is not None
