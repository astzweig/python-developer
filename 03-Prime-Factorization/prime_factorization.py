def get_prime_factors(number: int) -> list[int]:
    factors = []
    if (number > 1):
        for divisor in range(2, number + 1):
            while is_divisible_by(number, divisor):
                factors.append(divisor)
                number /= divisor
    return factors

def is_divisible_by(number: int, divisor: int) ->  bool:
    return number % divisor == 0
