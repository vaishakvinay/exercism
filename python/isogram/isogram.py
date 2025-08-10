def is_isogram(string):
    iso = string.lower()
    letters = [c for c in iso if c.isalpha()]
    return len(set(letters)) == len(letters)