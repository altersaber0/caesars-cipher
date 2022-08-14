import unittest
from caesars_cipher import CaesarsCipher
import string

class TestConstructor(unittest.TestCase):

    def test_alphabet_argument_validation(self):
        self.assertRaises(TypeError, CaesarsCipher, alphabet=123123)
        self.assertRaises(ValueError, CaesarsCipher, alphabet="^&?/abcdefg123")
    
class TestEncryption(unittest.TestCase):

    def test_message_argument_validation(self):
        cipher = CaesarsCipher(alphabet=string.ascii_lowercase)
        self.assertRaises(ValueError, cipher.encrypt, 123, shift=1)
        self.assertRaises(ValueError, cipher.encrypt, None, shift=1)
    
    def test_languages(self):
        cipher_en = CaesarsCipher(alphabet=string.ascii_lowercase)
        cipher_ru = CaesarsCipher(alphabet="абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
        cipher_ua = CaesarsCipher(alphabet="абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")
        self.assertEqual(cipher_en.encrypt("aBcDeFg", shift=5), "fGhIjKl")
        self.assertEqual(cipher_ru.encrypt("аБвГдЕё", shift=5), "еЁжЗиЙк")
        self.assertEqual(cipher_ua.encrypt("аБвГґДе", shift=5), "дЕєЖзИі")
    
    def test_shift_argument_validation(self):
        cipher = CaesarsCipher(alphabet=string.ascii_lowercase)
        self.assertRaises(ValueError, cipher.encrypt, "abcdefg", shift=0)
        self.assertRaises(ValueError, cipher.encrypt, "abcdefg", shift=-1)

    def test_shift_overflow(self):
        cipher = CaesarsCipher(alphabet=string.ascii_lowercase)
        self.assertEqual(cipher.encrypt("Pizza", shift=5), "Uneef")
        self.assertEqual(cipher.encrypt("abcdefg", shift=27), "bcdefgh")

class TestDecryption(unittest.TestCase):
    
    def test_output(self):
        cipher = CaesarsCipher(alphabet=string.ascii_lowercase)
        self.assertIn("Pizza", cipher.decrypt("Uneef"))


if __name__ == "__main__":
    unittest.main()