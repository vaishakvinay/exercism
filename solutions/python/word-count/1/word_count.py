import re

def count_words(sentence):
    # lowercase everything
    sentence = sentence.lower()

    # regex to match words:
    # - letters or digits
    # - may contain an internal apostrophe (e.g. can't, don't, they're)
    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", sentence)

    # count them
    result = {}
    for w in words:
        if w in result:
            result[w] += 1
        else:
            result[w] = 1

    return result
