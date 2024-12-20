from fastapi import APIRouter, HTTPException, status

from api.authorization import Authorization
from api.dependencies import dep
from shared.dto import CreateUserDto, UpdateUserDto, UserDto

service = dep.services.users

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/this", response_model=UserDto)
async def get_current_user(user: Authorization) -> UserDto:
    return user


@router.get("/{user_id}", response_model=UserDto)
async def get(user_id: int) -> UserDto:
    entity = await service.get_by_id(user_id)
    return entity


@router.get("/", response_model=list[UserDto])
async def get_all() -> list[UserDto]:
    users = await service.get_all()
    return list(users)


@router.put("/", response_model=UserDto)
async def update(dto: UpdateUserDto, identity: Authorization):
    if dto.id != identity.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't update other users",
        )

    return await service.update(dto)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(dto: CreateUserDto):
    user_id = await service.create(dto)
    return {"id": user_id}


@router.delete("/{user_id}", status_code=status.HTTP_200_OK, dependencies=[])
async def delete(user_id: int, user: Authorization):
    if user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't delete other users",
        )

    await service.delete(user_id)
    return {"msg": f"deleted user {user_id}"}
