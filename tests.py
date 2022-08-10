from unicodedata import name
import unittest
import caesars_cipher


class TestCipher(unittest.TestCase):

    def test_message_argument_validity(self):
        self.assertRaises(ValueError, caesars_cipher.cipher, 123, shift=1, language="en")
        self.assertRaises(ValueError, caesars_cipher.cipher, None, shift=1, language="en")
    
    def test_languages(self):
        self.assertEqual(caesars_cipher.cipher("aBcDeFg", shift=5, language="en"), "fGhIjKl")
        self.assertEqual(caesars_cipher.cipher("аБвГдЕё", shift=5, language="ru"), "еЁжЗиЙк")
        self.assertEqual(caesars_cipher.cipher("аБвГґДе", shift=5, language="ua"), "дЕєЖзИі")
        self.assertRaises(ValueError, caesars_cipher.cipher, "abcdefg", shift=1, language="de")
    
    def test_shift_argument_validity(self):
        self.assertRaises(ValueError, caesars_cipher.cipher, "abcdefg", shift=0, language="en")
        self.assertRaises(ValueError, caesars_cipher.cipher, "abcdefg", shift=-1, language="en")

    def test_shift_overflow(self):
        self.assertEqual(caesars_cipher.cipher("Pizza", shift=5, language="en"), "Uneef")
        self.assertEqual(caesars_cipher.cipher("abcdefg", shift=27, language="en"), "bcdefgh")

class TestDecipher(unittest.TestCase):
    ...


if __name__ == "__main__":
    unittest.main()