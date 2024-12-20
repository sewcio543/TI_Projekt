from fastapi import FastAPI, HTTPException, status

from api import settings
from api.dependencies import dep
from api.shared.authorization import Authorization
from api.shared.cors import add_cors_middleware
from shared.dto import CreateUserDto, UpdateUserDto, UserDto

service = dep.services.users

app = FastAPI(title="GrudgeHub People API")
add_cors_middleware(
    app,
    origins=[
        settings.FRONTEND_URL,
        settings.CONTENT_API_URL,
    ],
)


@app.get("/this", response_model=UserDto)
async def get_current_user(user: Authorization) -> UserDto:
    return user


@app.get("/{user_id}", response_model=UserDto)
async def get(user_id: int) -> UserDto:
    entity = await service.get_by_id(user_id)
    return entity


@app.get("/", response_model=list[UserDto])
async def get_all() -> list[UserDto]:
    users = await service.get_all()
    return list(users)


@app.put("/", response_model=UserDto)
async def update(dto: UpdateUserDto, identity: Authorization):
    if dto.id != identity.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't update other users",
        )

    return await service.update(dto)


@app.post("/", status_code=status.HTTP_201_CREATED)
async def create(dto: CreateUserDto):
    user_id = await service.create(dto)
    return {"id": user_id}


@app.delete("/{user_id}", status_code=status.HTTP_200_OK, dependencies=[])
async def delete(user_id: int, user: Authorization):
    if user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't delete other users",
        )

    await service.delete(user_id)
    return {"msg": f"deleted user {user_id}"}
