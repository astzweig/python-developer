import unittest
from levenshtein import edit_distance

class TestLevenshteinDistance(unittest.TestCase):
    def test_distanceOfTwoEmptyWordsIsZero(self):
        self.assertEqual(0, edit_distance('', ''))

    def test_distanceOfSameWordIsZero(self):
        word = 'whatwg'
        self.assertEqual(0, edit_distance(word, word))

    def test_distanceToEmptyWordIsWordLength(self):
        word = 'whatwg'
        self.assertEqual(len(word), edit_distance(word, ''))

    def test_distanceOfDifferentCharsIsOne(self):
        self.assertEqual(1, edit_distance('a', 'b'))

    def test_distanceOfSameLengthWordsIsAmountOfDifferentChars(self):
        self.assertEqual(1, edit_distance('hallo', 'hOllo'))
        self.assertEqual(2, edit_distance('HAllo', 'hallo'))

    def test_distanceForAdditionalLetterIsOne(self):
        self.assertEqual(1, edit_distance('hallo', 'halloo'))
