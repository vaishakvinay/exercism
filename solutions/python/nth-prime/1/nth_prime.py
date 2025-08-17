def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')

    primes = [2]
    n = 2 #number to check if prime
    while len(primes) < number:
        n += 1                     # move to next number
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)

    return primes[-1]              # last prime in the list


