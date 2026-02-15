subjects = [
    "the house that Jack built.",
    "the malt",
    "the rat",
    "the cat",
    "the dog",
    "the cow with the crumpled horn",
    "the maiden all forlorn",
    "the man all tattered and torn",
    "the priest all shaven and shorn",
    "the rooster that crowed in the morn",
    "the farmer sowing his corn",
    "the horse and the hound and the horn"
]

actions = [
    "",
    "that lay in ",
    "that ate ",
    "that killed ",
    "that worried ",
    "that tossed ",
    "that milked ",
    "that kissed ",
    "that married ",
    "that woke ",
    "that kept ",
    "that belonged to "
]


def recite(start_verse, end_verse):

    verses = []

    for verse in range(start_verse, end_verse + 1):

        index = verse - 1
        line = "This is "

        
        for j in range(index, -1, -1):

            line += subjects[j]

            if j > 0:
                line += " " + actions[j]

        verses.append(line)

    return verses
