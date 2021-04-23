def get_prime_factors(number: int) -> list[int]:
    factors = []
    if (number > 1):
        if (number % 2 == 0):
            factors.append(2)
            number //= 2
        if (number > 1):
            factors.append(number)
    return factors
