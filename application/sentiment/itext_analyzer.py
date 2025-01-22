from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ITextAnalyzer(ABC):

    @abstractmethod
    def translate(self, to: str) -> "ITextAnalyzer":
        raise NotImplementedError

    @property
    def sentiment(self):
        raise NotImplementedError
