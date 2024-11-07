import nltk
from nltk.tokenize import word_tokenize
import string
from typing import List

# Download required NLTK data
nltk.download('punkt')

class TextPreprocessor:
    @staticmethod
    def tokenize(text: str) -> List[str]:
        return word_tokenize(text)
    
    @staticmethod
    def remove_punctuation(text: str) -> str:
        return text.translate(str.maketrans("", "", string.punctuation))
    
    @staticmethod
    def pad_text(text: str, length: int = 100) -> str:
        words = text.split()
        if len(words) >= length:
            return " ".join(words[:length])
        else:
            padding = ["<PAD>"] * (length - len(words))
            return " ".join(words + padding)