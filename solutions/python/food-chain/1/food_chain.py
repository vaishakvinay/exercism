animals = [
    "fly",
    "spider",
    "bird",
    "cat",
    "dog",
    "goat",
    "cow",
    "horse"
]

comments = {
    "fly": "",
    "spider": "It wriggled and jiggled and tickled inside her.",
    "bird": "How absurd to swallow a bird!",
    "cat": "Imagine that, to swallow a cat!",
    "dog": "What a hog, to swallow a dog!",
    "goat": "Just opened her throat and swallowed a goat!",
    "cow": "I don't know how she swallowed a cow!",
    "horse": "She's dead, of course!"
}


def recite(start_verse, end_verse):
    verses = []

    for i in range(start_verse, end_verse + 1):

        animal = animals[i - 1]
        lines = []

    
        lines.append(f"I know an old lady who swallowed a {animal}.")

       
        if animal == "horse":
            lines.append(comments["horse"])
            verses.extend(lines)

            if i != end_verse:
                verses.append("")
            continue

       
        if comments[animal]:
            lines.append(comments[animal])

        
        for j in range(i - 1, 0, -1):

            current = animals[j]
            previous = animals[j - 1]

            if previous == "spider":
                previous += " that wriggled and jiggled and tickled inside her"

            lines.append(
                f"She swallowed the {current} to catch the {previous}."
            )

       
        lines.append(
            "I don't know why she swallowed the fly. Perhaps she'll die."
        )

        verses.extend(lines)

        if i != end_verse:
            verses.append("")

    return verses

