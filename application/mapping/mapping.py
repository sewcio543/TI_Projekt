from domain.models.db_models import Comment, Grudge, Post, User
from shared.dto.comment_dto import CommentDto, CreateCommentDto, UpdateCommentDto
from shared.dto.grudge_dto import CreateGrudgeDto, GrudgeDto
from shared.dto.post_dto import CreatePostDto, PostDto, UpdatePostDto
from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto

UserDtoType = UserDto | CreateUserDto | UpdateUserDto
PostDtoType = PostDto | CreatePostDto | UpdatePostDto
CommentDtoType = CommentDto | CreateCommentDto | UpdateCommentDto
GrudgeDtoType = GrudgeDto | CreateGrudgeDto


def user_to_dto(user: User) -> UserDto:
    return UserDto(id=user.id, login=user.login)


def dto_to_user(dto: UserDtoType) -> User:
    user = User(login=dto.login)

    if isinstance(dto, (UserDto, UpdateUserDto)):
        user.id = dto.id

    return user


def post_to_dto(post: Post) -> PostDto:
    return PostDto(id=post.id, content=post.content, user_id=post.user_id)


def dto_to_post(dto: PostDtoType) -> Post:
    post = Post(content=dto.content)

    if isinstance(dto, (PostDto, CreatePostDto)):
        post.user_id = dto.user_id

    if isinstance(dto, (PostDto, UpdatePostDto)):
        post.id = dto.id

    return post


def comment_to_dto(post: Comment) -> CommentDto:
    return CommentDto(
        id=post.id,
        content=post.content,
        user_id=post.user_id,
        post_id=post.post_id,
    )


def dto_to_comment(dto: CommentDtoType) -> Comment:
    comment = Comment(content=dto.content)

    if isinstance(dto, (CommentDto, CreateCommentDto)):
        comment.user_id = dto.user_id
        comment.post_id = dto.post_id

    if isinstance(dto, (CommentDto, UpdateCommentDto)):
        comment.id = dto.id

    return comment


def grudge_to_dto(post: Grudge) -> GrudgeDto:
    return GrudgeDto(
        id=post.id,
        user_id=post.user_id,
        post_id=post.post_id,
    )


def dto_to_grudge(dto: GrudgeDtoType) -> Grudge:
    grudge = Grudge(user_id=dto.user_id, post_id=dto.post_id)

    if isinstance(dto, GrudgeDto):
        grudge.id = dto.id

    return grudge
