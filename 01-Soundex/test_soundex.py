import unittest
from soundex import soundex

def first_char(word: str) -> str:
    return word[0]

class TestSoundex(unittest.TestCase):
    def test_retainsSoleCharOfWord(self):
        self.assertEqual('A', first_char(soundex('A')))
        self.assertEqual('B', first_char(soundex('B')))

    def test_zeroPadsSingleCharWord(self):
        self.assertEqual('A000', soundex('A'))

    def test_replacesConsonantsWithDigit(self):
        self.assertEqual('A400', soundex('Al'))

    def test_contractConsecutiveConsonants(self):
        self.assertEqual('A400', soundex('All'))

    def test_removesHandW(self):
        self.assertEqual('A000', soundex('Ahw'))

    def test_contractsConsonantsSeparatedByHorW(self):
        self.assertEqual('A400', soundex('Alhl'))

    def test_removesVowels(self):
        self.assertEqual('A000', soundex('Aaaa'))

    def test_retainsCaseOfFirstChar(self):
        self.assertEqual('a000', soundex('a'))
        self.assertEqual('l000', soundex('l'))
        self.assertEqual('H000', soundex('H'))
