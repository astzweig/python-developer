import unittest
from soundex import soundex

def first_letter(word: str) -> str:
    return word[0]

class TestSoundex(unittest.TestCase):
    def test_retainsSoleLetterOfWord(self):
        self.assertEqual('A', first_letter(soundex('A')))
        self.assertEqual('B', first_letter(soundex('B')))


