import unittest
from prime_factorization import get_prime_factors

class TestGetPrimeFactors(unittest.TestCase):
    def test_returnsAnEmptyListWhenNumberIsOne(self):
        self.assertEqual([], get_prime_factors(1))

    def test_returnsAListWithTheNumberTwoWhenNumberIsTwo(self):
        self.assertEqual([2], get_prime_factors(2))
