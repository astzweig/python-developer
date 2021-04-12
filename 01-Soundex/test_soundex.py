import unittest
from soundex import soundex

def first_letter(word: str) -> str:
    return word[0]

class TestSoundex(unittest.TestCase):
    def test_retainsSoleLetterOfWord(self):
        self.assertEqual('A', first_letter(soundex('A')))
        self.assertEqual('B', first_letter(soundex('B')))

    def test_zeroPadsSingleLetterWord(self):
        self.assertEqual('A000', soundex('A'))

    def test_replacesConsonantsWithDigit(self):
        self.assertEqual('A400', soundex('Al'))

    def test_contractConsecutiveConsonants(self):
        self.assertEqual('A400', soundex('All'))
