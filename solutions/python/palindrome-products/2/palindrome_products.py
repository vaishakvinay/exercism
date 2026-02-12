def largest(min_factor, max_factor):

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

  
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    best_palindrome = None
    best_factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):

            product = i * j

            if is_palindrome(product):

                if best_palindrome is None or product > best_palindrome:
                    best_palindrome = product
                    best_factors = [[i, j]]

                elif product == best_palindrome:
                    best_factors.append([i, j])

    
    if best_palindrome is None:
        return None, []


    best_factors = [sorted(pair) for pair in best_factors]
    best_factors.sort()

    return best_palindrome, best_factors


def smallest(min_factor, max_factor):

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    best_palindrome = None
    best_factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):

            product = i * j

            if is_palindrome(product):

                if best_palindrome is None or product < best_palindrome:
                    best_palindrome = product
                    best_factors = [[i, j]]

                elif product == best_palindrome:
                    best_factors.append([i, j])

    if best_palindrome is None:
        return None, []

    best_factors = [sorted(pair) for pair in best_factors]
    best_factors.sort()

    return best_palindrome, best_factors




