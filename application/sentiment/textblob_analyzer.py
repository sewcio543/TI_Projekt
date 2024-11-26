from textblob import TextBlob
from .itext_analyzer import ITextAnalyzer

class TextBlobAnalyzer(ITextAnalyzer):
        
    def __init__(self, text: str):
        self._text = text
        self._blob = TextBlob(text)
        
    def translate(self, to: str) -> str:
         # todo: TextBlob.translate() is depreciated, might need to use Google Translate API..
        return self._blob #.translate(to=to)
        
    @property
    def sentiment(self):
        return self._blob.sentiment.polarity    
        