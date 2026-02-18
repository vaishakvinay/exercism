days = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}

gifts = {
    1: "a Partridge in a Pear Tree.",
    2: "two Turtle Doves,",
    3: "three French Hens,",
    4: "four Calling Birds,",
    5: "five Gold Rings,",
    6: "six Geese-a-Laying,",
    7: "seven Swans-a-Swimming,",
    8: "eight Maids-a-Milking,",
    9: "nine Ladies Dancing,",
    10: "ten Lords-a-Leaping,",
    11: "eleven Pipers Piping,",
    12: "twelve Drummers Drumming,",
}


def recite(start_verse, end_verse):
    verses = []

    for day in range(start_verse, end_verse + 1):
        line = f"On the {days[day]} day of Christmas my true love gave to me: "

        parts = []
        for gift_day in range(day, 0, -1):
            if gift_day == 1 and day > 1:
                parts.append("and " + gifts[gift_day])
            else:
                parts.append(gifts[gift_day])

        line += " ".join(parts)
        verses.append(line)

    return verses

