"""Prime factorization module."""


def factors(value):
    """Return the prime factors of a given natural number."""

    prime_factors = []
    divisor = 2

   
    while divisor * divisor <= value:

        while value % divisor == 0:
            prime_factors.append(divisor)
            value //= divisor

        divisor += 1

   
    if value > 1:
        prime_factors.append(value)

    return prime_factors