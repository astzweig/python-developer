import unittest
from tenis_points import get_tenis_points_of_all_players

class TestGetTenisPointsForAllPlayers(unittest.TestCase):
    def test_returnsZeroIfGivenEmptyList(self):
        self.assertEqual((0, 0), get_tenis_points_of_all_players([]))

    def test_returnsSumIfOnlyOneRoundIsGiven(self):
        result = get_tenis_points_of_all_players([1])
        self.assertEqual((1, 2), result)
