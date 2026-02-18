ONES = {
    0: "zero", 1: "one", 2: "two", 3: "three",
    4: "four", 5: "five", 6: "six", 7: "seven",
    8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen"
}

TENS = {
    20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty",
    70: "seventy", 80: "eighty", 90: "ninety"
}

SCALES = ["", "thousand", "million", "billion"]


def say(number):
    
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    if number<20:
        return ONES[number]

    if number<100:
        if number %10==0:
            return TENS[number]
        return TENS[(number // 10) * 10] + "-" + ONES[number % 10]
    
    if 100 <= number < 1000:

        hundreds = ONES[number // 100] + " hundred"
        remainder = number % 100

        if remainder == 0:
            return hundreds

        if remainder < 20:
            return hundreds + " " + ONES[remainder]

        if remainder % 10 == 0:
            return hundreds + " " + TENS[remainder]

        return (
            hundreds
            + " "
            + TENS[(remainder // 10) * 10]
            + "-"
            + ONES[remainder % 10]
        )

    if number >= 1000:
            chunks = []
            n = number
            
            while n > 0:
                chunks.append(n % 1000)
                n //= 1000
            words = []

    for i, chunk in enumerate(chunks):
    
        if chunk == 0:
            continue
        
        chunk_words = say(chunk)
        scale_word = SCALES[i]

        if scale_word:
            words.append(chunk_words + " " + scale_word)
        else:
            words.append(chunk_words)

    return " ".join(reversed(words))