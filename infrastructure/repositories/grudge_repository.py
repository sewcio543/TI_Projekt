from domain.contracts.igrudge_repository import IGrudgeRepository
from domain.models.db_models import Grudge
from infrastructure.repositories.repository import Repository


class GrudgeRepository(Repository[Grudge], IGrudgeRepository):
    model = Grudge

    async def exists(self, id: int) -> bool:
        entity = await self.session.get(self.model, id)
        return entity is not None
