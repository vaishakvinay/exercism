def factors(value):
    result = []
    i = 2
    while value > 1:
        while value % i == 0:
            result.append(i)
            value //= i
        i += 1
    return result
