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
    def to_entity(cls, dto: UserDtoType) -> User:
        user = User(login=dto.login)

        if isinstance(dto, (UserDto, UpdateUserDto)):
            user.id = dto.id

        return user

    @classmethod
    def update(cls, entity: User, dto: UpdateUserDto) -> User:
        entity.login = dto.login
        return entity


class PostMapper(DtoMapper[Post]):
    @classmethod
    def to_dto(cls, entity: Post) -> PostDto:
        user_dto = UserDto(id=entity.user_id, login=entity.user.login)
        return PostDto(id=entity.id, content=entity.content, user=user_dto)

    @classmethod
    def to_entity(cls, dto: PostDtoType) -> Post:
        post = Post(content=dto.content)

        if isinstance(dto, CreatePostDto):
            post.user_id = dto.user_id

        if isinstance(dto, PostDto):
            post.user_id = dto.user.id  # type: ignore

        if isinstance(dto, (PostDto, UpdatePostDto)):
            post.id = dto.id

        return post

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
    def to_entity(cls, dto: CommentDtoType) -> Comment:
        comment = Comment(content=dto.content)

        if isinstance(dto, CreateCommentDto):
            comment.user_id = dto.user_id
            comment.post_id = dto.post_id

        if isinstance(dto, CommentDto):
            comment.user_id = dto.user.id  # type: ignore
            comment.post_id = dto.post.id  # type: ignore

        if isinstance(dto, (CommentDto, UpdateCommentDto)):
            comment.id = dto.id

        return comment

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
    def to_entity(cls, dto: GrudgeDtoType) -> Grudge:
        grudge = Grudge()

        if isinstance(dto, CreateGrudgeDto):
            grudge.user_id = dto.user_id
            grudge.post_id = dto.post_id

        if isinstance(dto, GrudgeDto):
            grudge.id = dto.id

        return grudge

    @classmethod
    def update(cls, entity: Grudge, dto: GrudgeDto) -> Grudge:
        return entity
