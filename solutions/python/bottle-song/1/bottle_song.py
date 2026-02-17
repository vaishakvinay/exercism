numbers = [
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten"
]


def recite(start, take=1):

    verses = []

    for n in range(start, start - take, -1):

        current = numbers[n].capitalize()
        next_word = numbers[n - 1]

        bottle_current = "bottle" if n == 1 else "bottles"
        bottle_next = "bottle" if (n - 1) == 1 else "bottles"

        verses.append(
            f"{current} green {bottle_current} hanging on the wall,"
        )
        verses.append(
            f"{current} green {bottle_current} hanging on the wall,"
        )
        verses.append(
            "And if one green bottle should accidentally fall,"
        )
        verses.append(
            f"There'll be {next_word} green {bottle_next} hanging on the wall."
        )

      
        if n != start - take + 1:
            verses.append("")

    return verses
