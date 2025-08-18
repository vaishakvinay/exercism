gifts = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves,",
    "three French Hens,",
    "four Calling Birds,",
    "five Gold Rings,",
    "six Geese-a-Laying,",
    "seven Swans-a-Swimming,",
    "eight Maids-a-Milking,",
    "nine Ladies Dancing,",
    "ten Lords-a-Leaping,",
    "eleven Pipers Piping,",
    "twelve Drummers Drumming,"
]
days = ("first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")



def recite(start_verse, end_verse):
    result = []
    verses = []
    for day_num in range(start_verse, end_verse + 1):
        line = f"On the {days[day_num-1]} day of Christmas my true love gave to me: "
        gifts_list = []
        for gift in range(day_num, 0, -1):
            if gift == 1 and day_num > 1:
                gifts_list.append("and " + gifts[0])
            else:
                gifts_list.append(gifts[gift-1])
        line += " ".join(gifts_list)
        verses.append(line)
    return verses