import random
from nltk.corpus import wordnet
import nltk

# Download required NLTK data
nltk.download('wordnet')

class TextAugmenter:
    @staticmethod
    def synonym_replacement(sentence: str, n: int = 1) -> str:
        words = sentence.split()
        new_words = words.copy()
        
        for _ in range(n):
            if not words:
                break
                
            word_to_replace = random.choice(words)
            synonyms = []
            
            for syn in wordnet.synsets(word_to_replace):
                for lemma in syn.lemmas():
                    if lemma.name() != word_to_replace:
                        synonyms.append(lemma.name())
            
            if synonyms:
                synonym = random.choice(synonyms)
                new_words = [synonym if word == word_to_replace else word for word in new_words]
        
        return ' '.join(new_words)

    @staticmethod
    def random_insertion(sentence: str, n: int = 1) -> str:
        words = sentence.split()
        new_words = words.copy()
        
        for _ in range(n):
            if not words:
                break
                
            # Get a random word from the sentence
            insert_word = random.choice(words)
            # Insert it at a random position
            insert_pos = random.randint(0, len(new_words))
            new_words.insert(insert_pos, insert_word)
        
        return ' '.join(new_words)