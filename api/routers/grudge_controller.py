from fastapi import APIRouter, HTTPException, status

from api.dependencies import dep
from api.routers.identity_controller import Authorization
from shared.dto import CreateGrudgeDto, GrudgeDto

service = dep.services.grudges

router = APIRouter(prefix="/grudge", tags=["grudge"])


@router.get("/{grudge_id}", response_model=GrudgeDto)
async def get(grudge_id: int) -> GrudgeDto:
    entity = await service.get_by_id(grudge_id)
    return entity


@router.get("/", response_model=list[GrudgeDto])
async def get_all() -> list[GrudgeDto]:
    posts = await service.get_all()
    return list(posts)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(post: CreateGrudgeDto, user: Authorization):
    if post.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't create grudges for other users",
        )

    grudge_id = await service.create(post)
    return {"id": grudge_id}


@router.delete("/{grudge_id}", status_code=status.HTTP_200_OK)
async def delete(grudge_id: int, user: Authorization):
    grudge = await service.get_by_id(grudge_id)

    if grudge is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This grudge does not exist",
        )

    if grudge.user.id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't delete grudges from other users",
        )

    await service.delete(grudge_id)
    return {"msg": f"deleted grudge {grudge_id}"}
