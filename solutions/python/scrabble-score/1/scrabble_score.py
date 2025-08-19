def score(word):
    scores = {
    "AEIOULNRST": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10,
     }
    count=0
    word=word.upper()
    for key, value in scores.items():
        for char in word:
            if char in key:
                count+=value

    return count

