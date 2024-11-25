from fastapi import APIRouter, HTTPException, status

from api.dependencies import dep
from api.routers.identity_controller import Authorization
from shared.dto import CreatePostDto, PostDto, UpdatePostDto

service = dep.services.posts
moderator = dep.moderator

router = APIRouter(prefix="/post", tags=["post"])


@router.get("/{post_id}", response_model=PostDto)
async def get(post_id: int) -> PostDto:
    entity = await service.get_by_id(post_id)
    return entity


@router.get("/", response_model=list[PostDto])
async def get_all() -> list[PostDto]:
    posts = await service.get_all()
    return list(posts)


@router.put("/{post_id}", response_model=PostDto)
async def update(post_id: int, dto: UpdatePostDto, user: Authorization):
    if post_id != dto.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="id in path and in body do not match",
        )

    post = await service.get_by_id(post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This post does not exist",
        )

    if post.user.id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't update other users' posts",
        )

    return await service.update(dto)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(dto: CreatePostDto, user: Authorization):
    if dto.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't create posts for other users",
        )
    
    if not moderator.allows_content(dto.content):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This content is not allowed (to positive)",
        )
    
    post_id = await service.create(dto)
    return {"id": post_id}


@router.delete("/{post_id}", status_code=status.HTTP_200_OK)
async def delete(post_id: int, user: Authorization):
    post = await service.get_by_id(post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This post does not exist",
        )

    if post.user.id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't delete other users' posts",
        )

    await service.delete(post_id)
    return {"msg": f"deleted post {post_id}"}
