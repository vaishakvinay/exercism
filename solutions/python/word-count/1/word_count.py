import re

def count_words(sentence):
    
    sentence = sentence.lower()


    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", sentence.lower())


    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

