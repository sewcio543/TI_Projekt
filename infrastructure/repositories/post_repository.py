from domain.contracts.ipost_repository import IPostRepository
from infrastructure.repositories.repository import Repository
from domain.models.db_models import Post


class PostRepository(Repository[Post], IPostRepository):
    model = Post

    async def exists(self, id: int) -> bool:
        entity = await self.session.get(self.model, id)
        return entity is not None
