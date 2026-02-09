def abbreviate(words):
    text = words.replace("-", " ").replace("_", " ").split()

    new = []

    for ch in text:
        new.append(ch[0].upper())

    return "".join(new)
