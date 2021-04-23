import unittest
from tenis_points import get_tenis_points_of_all_players

class TestGetTenisPointsForAllPlayers(unittest.TestCase):
    def test_returnsZeroIfGivenEmptyList(self):
        self.assertEqual((0, 0), get_tenis_points_of_all_players([]))

    def test_returnsSumIfOnlyOneRoundIsGiven(self):
        result = get_tenis_points_of_all_players([1])
        self.assertEqual((1, 2), result)

    def test_multipliesPointsOfSecondRoundIfGiven2OnFirst(self):
        result = get_tenis_points_of_all_players([2, 1])
        self.assertEqual((4, 3), result)

    def test_multipliesPointsOfThirdRoundIfGiven3OnFirst(self):
        result = get_tenis_points_of_all_players([3, 3, 3])
        self.assertEqual((12, 0), result)

    def test_multipliesPointsTwoTimesIfGiven3And2(self):
        result = get_tenis_points_of_all_players([3, 2, 3])
        self.assertEqual((14, 1), result)
