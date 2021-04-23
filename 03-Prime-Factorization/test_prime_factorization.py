import unittest
from prime_factorization import get_prime_factors

class TestGetPrimeFactors(unittest.TestCase):
    def test_returnsAnEmptyListWhenNumberIsOne(self):
        self.assertEqual([], get_prime_factors(1))

    def test_returnsListWithNumberTwoWhenNumberIsTwo(self):
        self.assertEqual([2], get_prime_factors(2))

    def test_returnsListWithNumberThreeWhenNumberIsThree(self):
        self.assertEqual([3], get_prime_factors(3))

    def test_returnsListWithTwoNumberTwosWhenNumberIsFour(self):
        self.assertEqual([2, 2], get_prime_factors(4))
