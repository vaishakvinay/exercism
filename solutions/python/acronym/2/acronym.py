import re

def abbreviate(words):
    # Match letters at start of string or after space, hyphen, or underscore
    letters = re.findall(r"(?:^|[ _-])([A-Za-z])", words)
    return "".join(letters).upper()
