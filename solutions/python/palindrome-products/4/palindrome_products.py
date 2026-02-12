def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    max_pal = None
    factors = []


    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):

            prod = i * j


            if max_pal is not None and prod < max_pal:
                break

            if is_palindrome(prod):

                if max_pal is None or prod > max_pal:
                    max_pal = prod
                    factors = [[i, j]]

                elif prod == max_pal:
                    factors.append([i, j])

   
    if max_pal is None:
        return None, []

    return max_pal, factors


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    min_pal = None
    factors = []

    
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):

            prod = i * j

            
            if min_pal is not None and prod > min_pal:
                break

            if is_palindrome(prod):

                if min_pal is None or prod < min_pal:
                    min_pal = prod
                    factors = [[i, j]]

                elif prod == min_pal:
                    factors.append([i, j])


    if min_pal is None:
        return None, []

    return min_pal, factors





