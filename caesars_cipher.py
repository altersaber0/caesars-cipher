import string
from typing import Optional

def cipher(message: str, /, *, shift: int, language: Optional[str] = "en") -> str:
    if type(shift) != int or shift < 1:
        raise ValueError("\"shift\" argument must be a positive integer")
    if type(message) != str or not any([char.isalpha() for char in message]):
        raise ValueError("\"message\" argument must be a string with at least 1 alphabetic character")
    if language == "en":
        alphabet = zip(string.ascii_lowercase, string.ascii_uppercase)

    shift = shift % 26

    for char in message:
        if not char.isalpha():
            continue
        lowercase = None
        if char.islower():
            lowercase = True
        else:
            lowercase = False
        
        alphabet_index = 0

        for letter_index, letter in enumerate(alphabet):
            if char in letter:
                alphabet_index = letter_index
                break
