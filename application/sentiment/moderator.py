from typing import Type
from pydantic import BaseModel, Field

from .imoderator import IModerator
from .itext_analyzer import ITextAnalyzer

    
class Moderator(IModerator, BaseModel):
        
    threshold: float = Field(min=-1, max=1, default=0)
    analyzer: Type[ITextAnalyzer]
    
    def analyze_sentiment(self, text: str) -> float:
        """
        Analyze sentiment of the text. Return value is in range from -1 to 1.
        Provided text is translated to English.
        
        args:
            text : text to anlyze 
        """
        blob = self.analyzer(text).translate(to='en')
        return blob.sentiment.polarity
    
    def allows_content(self, text: str) -> bool:
        """
        Return True if text is appropriate, False otherwise.
        
        args:
            text : text to analyze
        """
        if self.analyze_sentiment(text) > self.threshold:
            return False
        return True
    
    
    
    
