def proverb(*words, qualifier=None):
    lines = []

    for first, second in zip(words, words[1:]):
        lines.append(f"For want of a {first} the {second} was lost.")

    if words:
        first_word = words[0]
        if qualifier:
            first_word = f"{qualifier} {first_word}"
        lines.append(f"And all for the want of a {first_word}.")

    return lines

