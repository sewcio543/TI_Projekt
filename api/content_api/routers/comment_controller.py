from fastapi import APIRouter, HTTPException, status

from api.dependencies import dep
from api.shared.authorization import Authorization
from shared.dto import CommentDto, CreateCommentDto, UpdateCommentDto

service = dep.services.comments
moderator = dep.moderator

router = APIRouter(prefix="/comment", tags=["comment"])


@router.get("/{comment_id}", response_model=CommentDto)
async def get(comment_id: int) -> CommentDto:
    entity = await service.get_by_id(comment_id)
    return entity


@router.get("/post/{post_id}", response_model=list[CommentDto])
async def get_by_post_id(post_id: int) -> list[CommentDto]:
    comments = await service.get_by_post_id(post_id)
    return list(comments)


@router.get("/", response_model=list[CommentDto])
async def get_all() -> list[CommentDto]:
    comments = await service.get_all()
    return list(comments)


@router.put("/{comment_id}", response_model=CommentDto)
async def update(comment_id: int, dto: UpdateCommentDto, user: Authorization):
    if comment_id != dto.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="id in path and in body do not match",
        )

    comment = await service.get_by_id(comment_id)

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This comment does not exist",
        )

    if comment.user.id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't update other users' comments",
        )

    if not moderator.allows_content(dto.content):
        raise HTTPException(
            status_code=status.HTTP_418_IM_A_TEAPOT,
            detail="This content is not allowed (to positive)",
        )

    return await service.update(dto)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(dto: CreateCommentDto, user: Authorization):
    if dto.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't create comments for other users",
        )

    if not moderator.allows_content(dto.content):
        raise HTTPException(
            status_code=status.HTTP_418_IM_A_TEAPOT,
            detail="This content is not allowed (to positive)",
        )

    comment_id = await service.create(dto)
    return {"id": comment_id}


@router.delete("/{comment_id}", status_code=status.HTTP_200_OK)
async def delete(comment_id: int, user: Authorization):
    comment = await service.get_by_id(comment_id)

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This comment does not exist",
        )

    if comment.user.id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can't delete other users' comments",
        )

    await service.delete(comment_id)
    return {"msg": f"deleted comment {comment_id}"}
