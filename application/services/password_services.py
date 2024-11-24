from typing import Protocol


class IHashingContext(Protocol):
    def hash(self, secret: str, *args, **kwargs) -> str:
        raise NotImplementedError

    def verify(self, secret: str, hash: str, *args, **kwargs) -> bool:
        raise NotImplementedError


def check_password(password: str) -> bool:
    #! TODO
    return len(password) >= 2
