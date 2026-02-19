def prime(number):

    if number == 0:
        raise ValueError("there is no zeroth prime")

    count = 0
    candidate = 2

    while True:

        is_prime = True

        for i in range(2, int(candidate ** 0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break

        if is_prime:
            count += 1
            if count == number:
                return candidate

        candidate += 1
