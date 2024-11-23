from fastapi import APIRouter, status

from application.services.interfaces.ipost_service import IPostService
from shared.dto import CreatePostDto, PostDto, UpdatePostDto


class PostController:
    def __init__(self, service: IPostService) -> None:
        self.service = service
        self.router = APIRouter(prefix="/post", tags=["post"])
        self.router.add_api_route(
            "/{post_id}", self.get, response_model=PostDto, methods=["GET"]
        )
        self.router.add_api_route(
            "/", self.get_all, response_model=list[PostDto], methods=["GET"]
        )
        self.router.add_api_route("/{post_id}", self.update, methods=["PUT"])
        self.router.add_api_route(
            "/", self.create, status_code=status.HTTP_201_CREATED, methods=["POST"]
        )
        self.router.add_api_route(
            "/{post_id}",
            self.delete,
            status_code=status.HTTP_200_OK,
            methods=["DELETE"],
        )

    async def get(self, post_id: int) -> PostDto:
        entity = await self.service.get_by_id(post_id)
        return entity

    async def get_all(self) -> list[PostDto]:
        posts = await self.service.get_all()
        return list(posts)

    async def update(self, post_id: int, post: UpdatePostDto):
        if post_id != post.id:
            return {"error": "id in path and in body do not match"}
        return await self.service.update(post)

    async def create(self, post: CreatePostDto):
        post_id = await self.service.create(post)
        return {"id": post_id}

    async def delete(self, post_id: int):
        await self.service.delete(post_id)
        return {"msg": f"deleted post {post_id}"}
