from domain.models.db_models import User, Post
from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto
from shared.dto.post_dto import CreatePostDto, UpdatePostDto, PostDto

UserDtoType = UserDto | CreateUserDto | UpdateUserDto
PostDtoType = PostDto | CreatePostDto | UpdatePostDto


def user_to_dto(user: User) -> UserDto:
    return UserDto(id=user.id, login=user.login)


def dto_to_user(dto: UserDtoType) -> User:
    user = User(login=dto.login)

    if isinstance(dto, (UserDto, UpdateUserDto)):
        user.id = dto.id

    return user


def post_to_dto(post: Post) -> PostDto:
    return PostDto(id=post.id, content=post.content, user_id=post.user_id)


def dto_to_post(dto: PostDtoType) -> User:
    post = Post(content=dto.content, user_id=dto.user_id)

    if isinstance(dto, (PostDto, UpdatePostDto)):
        post.id = dto.id

    return post
