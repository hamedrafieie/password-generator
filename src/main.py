import random
import string
from abc import ABC, abstractmethod


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
