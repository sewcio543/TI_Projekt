from domain.models.db_models import User
from shared.dto.user_dto import CreateUserDto, UpdateUserDto, UserDto

DtoType = UserDto | CreateUserDto | UpdateUserDto


def user_to_dto(user: User) -> UserDto:
    return UserDto(id=user.id, login=user.login)


def dto_to_user(dto: DtoType) -> User:
    user = User(login=dto.login)

    if isinstance(dto, (UserDto, UpdateUserDto)):
        user.id = dto.id

    return user
