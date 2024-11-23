from fastapi import APIRouter, status

from application.services.interfaces.icomment_service import ICommentService
from shared.dto import CommentDto, CreateCommentDto, UpdateCommentDto


class CommentController:
    def __init__(self, service: ICommentService) -> None:
        self.service = service
        self.router = APIRouter(prefix="/comment", tags=["comment"])
        self.router.add_api_route(
            "/{comment_id}",
            self.get,
            response_model=CommentDto,
            methods=["GET"],
        )
        self.router.add_api_route(
            "/", self.get_all, response_model=list[CommentDto], methods=["GET"]
        )
        self.router.add_api_route("/{comment_id}", self.update, methods=["PUT"])
        self.router.add_api_route(
            "/",
            self.create,
            status_code=status.HTTP_201_CREATED,
            methods=["POST"],
        )
        self.router.add_api_route(
            "/{comment_id}",
            self.delete,
            status_code=status.HTTP_200_OK,
            methods=["DELETE"],
        )

    async def get(self, comment_id: int) -> CommentDto:
        entity = await self.service.get_by_id(comment_id)
        return entity

    async def get_all(self) -> list[CommentDto]:
        comments = await self.service.get_all()
        return list(comments)

    async def update(self, comment_id: int, comment: UpdateCommentDto):
        if comment_id != comment.id:
            return {"error": "id in path and in body do not match"}
        return await self.service.update(comment)

    async def create(self, comment: CreateCommentDto):
        comment_id = await self.service.create(comment)
        return {"id": comment_id}

    async def delete(self, comment_id: int):
        await self.service.delete(comment_id)
        return {"msg": f"deleted comment {comment_id}"}
