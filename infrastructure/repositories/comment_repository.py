from domain.contracts.icomment_repository import ICommentRepository
from domain.models.db_models import Comment
from infrastructure.repositories.repository import Repository


class CommentRepository(Repository[Comment], ICommentRepository):
    model = Comment

    async def exists(self, id: int) -> bool:
        entity = await self.session.get(self.model, id)
        return entity is not None
