from application.mapping.imapper import DtoMapper
from domain.models.db_models import Comment, Grudge, Post, User
from shared.dto.comment_dto import CommentDto, CreateCommentDto, UpdateCommentDto
from shared.dto.grudge_dto import CreateGrudgeDto, GrudgeDto
from shared.dto.post_dto import CreatePostDto, PostDto, UpdatePostDto
from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto

UserDtoType = UserDto | CreateUserDto | UpdateUserDto
PostDtoType = PostDto | CreatePostDto | UpdatePostDto
CommentDtoType = CommentDto | CreateCommentDto | UpdateCommentDto
GrudgeDtoType = GrudgeDto | CreateGrudgeDto


class UserMapper(DtoMapper[User]):
    @classmethod
    def to_dto(cls, entity: User) -> UserDto:
        return UserDto(id=entity.id, login=entity.login)

    @classmethod
    def to_entity(cls, dto: CreateUserDto) -> User:
        return User(login=dto.login, hashed_password=dto.password)

    @classmethod
    def update(cls, entity: User, dto: UpdateUserDto) -> User:
        entity.login = dto.login
        entity.hashed_password = dto.password
        return entity


class PostMapper(DtoMapper[Post]):
    @classmethod
    def to_dto(cls, entity: Post) -> PostDto:
        user_dto = UserDto(id=entity.user_id, login=entity.user.login)
        return PostDto(id=entity.id, content=entity.content, user=user_dto)

    @classmethod
    def to_entity(cls, dto: CreatePostDto) -> Post:
        return Post(content=dto.content, user_id=dto.user_id)

    @classmethod
    def update(cls, entity: Post, dto: UpdatePostDto) -> Post:
        entity.content = dto.content
        return entity


class CommentMapper(DtoMapper[Comment]):
    @classmethod
    def to_dto(cls, entity: Comment) -> CommentDto:
        user_dto = UserDto(id=entity.user_id, login=entity.user.login)
        post_dto = PostDto(
            id=entity.post_id,
            content=entity.post.content,
            user=user_dto,
        )
        return CommentDto(
            id=entity.id,
            content=entity.content,
            user=user_dto,
            post=post_dto,
        )

    @classmethod
    def to_entity(cls, dto: CreateCommentDto) -> Comment:
        return Comment(content=dto.content, user_id=dto.user_id, post_id=dto.post_id)

    @classmethod
    def update(cls, entity: Comment, dto: UpdateCommentDto) -> Comment:
        entity.content = dto.content
        return entity


class GrudgeMapper(DtoMapper[Grudge]):
    @classmethod
    def to_dto(cls, entity: Grudge) -> GrudgeDto:
        user_dto = UserDto(id=entity.user_id, login=entity.user.login)
        post_dto = PostDto(
            id=entity.post_id,
            content=entity.post.content,
            user=user_dto,
        )
        return GrudgeDto(id=entity.id, user=user_dto, post=post_dto)

    @classmethod
    def to_entity(cls, dto: CreateGrudgeDto) -> Grudge:
        return Grudge(user_id=dto.user_id, post_id=dto.post_id)

    @classmethod
    def update(cls, entity: Grudge, dto: GrudgeDto) -> Grudge:
        return entity
