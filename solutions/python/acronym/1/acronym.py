
def abbreviate(words):
    result = []
    words = words.replace("_", " ").replace("-", " ")

    for w in words.split():
        
            result.append(w[0].upper())

    return "".join(result)