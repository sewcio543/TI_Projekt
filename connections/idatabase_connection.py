from __future__ import annotations

import re
from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Self


class IDatabaseConnection(ABC):
    def __init__(self, connection: str) -> None:
        self._connection_string = connection

    @abstractmethod
    def connect(self, **kwargs) -> AsyncSession:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_env(cls) -> Self:
        raise NotImplementedError

    def _obfuscate_password(self) -> str:
        """Helper function to replace the password of a dsn with asterisks

        :param dsn: String of the dsn to obfuscate.
        :return: The obfuscated dsn string.
        """
        reg = (
            r"^(?P<conn>.*?):\/\/"
            r"(?P<user>.*?):(?P<passwd>.*)@"
            r"(?P<addr>[^\(]*):(?P<port>[^\)]*)\/"
            r"(?P<dbname>.*?)$"
        )
        return re.sub(
            reg,
            r"\g<conn>://\g<user>:*****@\g<addr>:\g<port>/\g<dbname>",
            self._connection_string,
        )

    @property
    def url(self) -> str:
        return self._obfuscate_password()
