from abc import ABC, abstractmethod

class IModerator(ABC):
    
    @abstractmethod
    def analyze_sentiment(self, text: str) -> float:
        """
        Analyze sentiment of the text. Return value is in range from -1 to 1.
        """
        raise NotImplementedError
    
    def moderate_content(self, text: str) -> bool:
        """
        Return True if text is appropriate, False otherwise.
        """
        raise NotImplementedError
        