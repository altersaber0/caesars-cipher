class CaesarsCipher:
    """Takes one kw-argument - a language alphabet in all lowercase."""

    def __init__(self, /, *, alphabet: str) -> None:
        if type(alphabet) != str:
            raise TypeError("Argument \"alphabet\" must be of type string")
        if any([char in " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789" for char in alphabet]):
            raise ValueError("\"alphabet\" argument string must not contain special symbols, digits or spaces")

        self.alphabet_lower = alphabet
    
    @property
    def __alphabet_upper(self) -> str:
        return self.alphabet_lower.upper()

    @property
    def __alphabet(self) -> list[tuple[str, str]]:
        return list(zip(self.alphabet_lower, self.__alphabet_upper))

    def set_alphabet(self, new_alphabet: str) -> None:
        """Change the alphabet to another language."""

        if type(new_alphabet) != str:
            raise TypeError("Argument \"new_alphabet\" must be of type string")

        self.alphabet_lower = new_alphabet


    def encrypt(self, message: str, /, *, shift: int) -> str:
        """Encrypt a message by shifting each letter in the alphabet of the given language."""

        # Validating "shift" argument
        if type(shift) != int or shift < 1:
            raise ValueError("\"shift\" argument must be a positive integer")

        # Preparing arguments for use
        shift = shift % len(self.__alphabet)

        # Validating "message" argument
        if type(message) != str or not any([char in self.alphabet_lower or char in self.__alphabet_upper for char in message]):
            raise ValueError("\"message\" argument must be a string with at least 1 character from the given alphabet")

        # Algorithm itself

        encrypted_message = ""

        for char in message:
            # Linear search of the current char in alphabet to get its index
            alphabet_index = None
            index_in_letter_tuple = None
            for letter_index, letter in enumerate(self.__alphabet):
                if char in letter:
                    alphabet_index = letter_index
                    # Getting which case the letter is in for future shifting
                    index_in_letter_tuple = letter.index(char)
                    break
            
            # Ignore all non-alphabetic characters
            if alphabet_index is None:
                encrypted_message += char
                continue

            # Get new letter by shifting index of old one
            shifted_index = (alphabet_index + shift) % len(self.__alphabet)
            shifted_letter = self.__alphabet[shifted_index][index_in_letter_tuple]

            encrypted_message += shifted_letter
            
        return encrypted_message


    def decrypt(self, message: str) -> list[str]:
        """Get a list of results from all possible shift sizes (depending on the alphabet)."""
        
        # Validating "message" argument
        if type(message) != str or not any([char in self.alphabet_lower or char in self.__alphabet_upper for char in message]):
            raise ValueError("\"message\" argument must be a string with at least 1 character from given alphabet")

        possible_results = []

        # Shifting by a different number len(alphabet)-1 times to get all possible results
        for i in range(1, len(self.__alphabet)):
            result = self.encrypt(message, shift=i)
            possible_results.append(result)
        
        return possible_results