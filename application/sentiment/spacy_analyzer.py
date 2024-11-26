
from .itext_analyzer import ITextAnalyzer



class SpacyAnalyzer(ITextAnalyzer):
        
    def __init__(self, text: str):
        self._text = text

    # todo to be implemented if spaCy installation error is resolved