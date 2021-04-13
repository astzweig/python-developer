import unittest
from levenshtein import edit_distance

class TestLevenshteinDistance(unittest.TestCase):
    def test_distanceOfTwoEmptyWordsIsZero(self):
        self.assertEqual(0, edit_distance('', ''))

    def test_distanceOfSameWordIsZero(self):
        word = 'whatwg'
        self.assertEqual(0, edit_distance(word, word))
