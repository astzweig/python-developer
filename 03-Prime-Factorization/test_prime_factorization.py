import unittest
from prime_factorization import get_prime_factors

class TestGetPrimeFactors(unittest.TestCase):
    def test_returnsAnEmptyListWhenNumberIsOne(self):
        self.assertEqual([], get_prime_factors(1))
