import unittest
from prime_factorization import get_prime_factors

class TestGetPrimeFactors(unittest.TestCase):
    def test_returnsAnEmptyListWhenNumberIsOne(self):
        self.assertEqual([], get_prime_factors(1))

    def test_returnsListWithNumberWhenNumberIsPrime(self):
        for prime in [2, 3, 5, 7]:
            self.assertEqual([prime], get_prime_factors(prime))

    def test_returnsListWithTwoNumberTwosWhenNumberIsFour(self):
        self.assertEqual([2, 2], get_prime_factors(4))

    def test_returnsListWithNumberTwoAndThreeWhenNumberIsSix(self):
        self.assertEqual([2, 3], get_prime_factors(6))
