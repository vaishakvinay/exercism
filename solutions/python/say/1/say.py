def say(number):
    ndict = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }

    sdict = {
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    trdict = {
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    tdict = {
        100: "hundred",
        1000: "thousand",
        1000000: "million",
        1000000000: "billion"
    }

    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    def two_digit(n):
        if n < 10:
            return ndict[n]
        elif n < 20:
            return sdict[n]
        else:
            tens = (n // 10) * 10
            ones = n % 10
            if ones == 0:
                return trdict[tens]
            else:
                return trdict[tens] + "-" + ndict[ones]

    def three_digit(n):
        if n < 100:
            return two_digit(n)
        else:
            hundreds = n // 100
            remainder = n % 100
            if remainder == 0:
                return ndict[hundreds] + " " + tdict[100]
            else:
                return ndict[hundreds] + " " + tdict[100] + " " + two_digit(remainder)

    if number == 0:
        return ndict[0]

    parts = []
    scales = [1000000000, 1000000, 1000, 1]
    for scale in scales:
        if number >= scale:
            chunk = number // scale
            number %= scale
            if chunk > 0:
                if scale >= 1000:
                    parts.append(three_digit(chunk) + " " + tdict[scale])
                else:
                    parts.append(three_digit(chunk))

    return " ".join(parts)
        