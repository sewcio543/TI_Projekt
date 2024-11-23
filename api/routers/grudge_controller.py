from fastapi import APIRouter, status

from application.services.interfaces.igrudge_service import IGrudgeService
from shared.dto import CreateGrudgeDto, GrudgeDto


class GrudgeController:
    def __init__(self, service: IGrudgeService) -> None:
        self.service = service
        self.router = APIRouter(prefix="/grudge", tags=["grudge"])
        self.router.add_api_route(
            "/{grudge_id}", self.get, response_model=GrudgeDto, methods=["GET"]
        )
        self.router.add_api_route(
            "/", self.get_all, response_model=list[GrudgeDto], methods=["GET"]
        )
        self.router.add_api_route(
            "/", self.create, status_code=status.HTTP_201_CREATED, methods=["POST"]
        )
        self.router.add_api_route(
            "/{grudge_id}",
            self.delete,
            status_code=status.HTTP_200_OK,
            methods=["DELETE"],
        )

    async def get(self, grudge_id: int) -> GrudgeDto:
        entity = await self.service.get_by_id(grudge_id)
        return entity

    async def get_all(self) -> list[GrudgeDto]:
        posts = await self.service.get_all()
        return list(posts)

    async def create(self, post: CreateGrudgeDto):
        grudge_id = await self.service.create(post)
        return {"id": grudge_id}

    async def delete(self, grudge_id: int):
        await self.service.delete(grudge_id)
        return {"msg": f"deleted post {grudge_id}"}
