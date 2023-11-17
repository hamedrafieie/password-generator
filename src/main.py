import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download('words')


class PasswordGenerator(ABC):
    """
    Base class for generating passwords.
    """
    @abstractmethod
    def generate(self) -> str:
        """
        Subclasses should override this method to generate password.
        """
        pass


class PinCodeGenerator(PasswordGenerator):
    """
    Class to generate a numeric pin code.
    """
    def __init__(self, length: int = 4):
        self.length: int = length

    def generate(self) -> str:
        """
        Generate a numeric pin code.
        """
        return ''.join(random.choice(string.digits) for _ in range(self.length))

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, include_capitalization: bool = False, include_numbers: bool = False, include_symbols: bool = False, length: int = 8):
        self.length: int = length
        self.include_numbers: bool = include_numbers
        self.include_symbols: bool = include_symbols
        self.include_capitalization: bool = include_capitalization
        self.source = string.ascii_lowercase
        if include_capitalization:
            self.source = string.ascii_letters
        if include_numbers:
            self.source += string.digits
        if include_symbols:
            self.source += string.punctuation

    def generate(self) -> str:
        result = ''.join(random.choice(self.source) for i in range(self.length))
        return f"your pasword is {result}"

    class MemorablePasswordGenerator(PasswordGenerator):
        def __init__(
            self,
            no_of_words: int = 5,
            separator: str = "-",
            capitalization: bool = False,
            vocabulary: Optional[List[str]] = None
        ):
            if vocabulary is None:
                vocabulary = nltk.corpus.words.words()  # edit this to any vocabulary list you want

            self.no_of_words: int = no_of_words
            self.separator: str = separator
            self.capitalization: bool = capitalization
            self.vocabulary: List[str] = vocabulary

        def generate(self) -> str:
            """
            Generate a password from a list of vocabulary words.
            """
            password_words = [random.choice(self.vocabulary) for _ in range(self.no_of_words)]
            if self.capitalization:
                password_words = [word.upper() for word in password_words]
            return self.separator.join(password_words)


if __name__ == "__main__":
    main()
