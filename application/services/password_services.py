from typing import Protocol


class IHashingContext(Protocol):
    def hash(self, secret: str, *args, **kwargs) -> str:
        raise NotImplementedError

    def verify(self, secret: str, hash: str, *args, **kwargs) -> bool:
        raise NotImplementedError


def check_password(password: str) -> bool:
    if len(password) < 5:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    return True
