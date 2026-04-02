def prime(number):

    if number == 0:
        raise ValueError("there is no zeroth prime")

    
    result = []
    candidate = 2

    while len(result) < number:

        prime_number = True

        for i in range(2, candidate):

            if candidate % i == 0:
                prime_number = False
                break

        if prime_number:
            result.append(candidate)

        candidate += 1

    return result[-1]
