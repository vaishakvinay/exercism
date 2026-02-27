def triplets_with_sum(number):
    result = []

    for a in range(1, number // 3 + 1):
        numerator = number * (number - 2 * a)
        denominator = 2 * (number - a)

       
        if denominator != 0 and numerator % denominator == 0:
            b = numerator // denominator
            c = number - a - b

            if a < b < c:
                result.append([a, b, c])

    return result