from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class ITextAnalyzer(ABC):
    
    @abstractmethod
    def translate(self, to: str) -> 'ITextAnalyzer':
        raise NotImplementedError
    
    @property
    def sentiment(self):
        raise NotImplementedError
        