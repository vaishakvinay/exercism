def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    f = []
    for num in range(1, number):
        if number % num == 0:
            f.append(num)
    if number == sum(f):
        return "perfect"
    if number < sum(f):
        return "abundant"
    if number > sum(f):
        return "deficient"