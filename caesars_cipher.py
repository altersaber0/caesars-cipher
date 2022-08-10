

def cipher(message: str, /, *, shift: int, language: str) -> str:
    # Validating "message" argument
    if type(shift) != int or shift < 1:
        raise ValueError("\"shift\" argument must be a positive integer")
    # Validating "shift" argument
    if type(message) != str or not any([char.isalpha() for char in message]):
        raise ValueError("\"message\" argument must be a string with at least 1 alphabetic character")
    # Validating "language" argument
    if language == "en":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
    elif language == "ru":
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    else:
        raise ValueError("\"language\" argument must be either \"en\" or \"ru\", other are not supported")

    # Preparing arguments for use
    alphabet = zip(alphabet, alphabet.upper())
    shift = shift % len(alphabet)

    # Algorithm itself
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
