

def cipher(message: str, /, *, shift: int, language: str) -> str:
    # Validating "message" argument
    if type(shift) != int or shift < 1:
        raise ValueError("\"shift\" argument must be a positive integer")

    # Validating "shift" argument
    if type(message) != str or not any([char.isalpha() for char in message]):
        raise ValueError("\"message\" argument must be a string with at least 1 alphabetic character")

    # Validating "language" argument
    if language == "en":
        alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    elif language == "ru":
        alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    else:
        raise ValueError("\"language\" argument must be either \"en\" or \"ru\", other are not supported")

    # Preparing arguments for use
    alphabet_upper = alphabet_lower.upper()
    alphabet = list(zip(alphabet_lower, alphabet_upper))
    shift = shift % len(alphabet)

    # Algorithm itself

    ciphered_message = ""

    for char in message:
        # Ignoring all non-alphabetic characters
        if not char.isalpha():
            ciphered_message += char
            continue

        # Getting which case the letter is in for future searching of alphabet
        if char.islower():
            lowercase = True
        else:
            lowercase = False

        # Linear search of the current char in alphabet to get its index
        alphabet_index = 0
        for letter_index, letter in enumerate(alphabet):
            if char in letter:
                alphabet_index = letter_index
                break

        # Getting new letter by shifting index of old one
        shifted_index = (alphabet_index + shift) % len(alphabet)
        if lowercase:
            shifted_letter = alphabet_lower[shifted_index]
        else:
            shifted_letter = alphabet_upper[shifted_index]

        ciphered_message += shifted_letter
        
    
    return ciphered_message

# print(cipher("Pizza", shift=5, language="en"))