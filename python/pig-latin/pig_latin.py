def translate(text):
    vowels = ("a", "e", "i", "o", "u")
    result = []

    for word in text.split():
        # Rule 1: Starts with vowel or special case
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            result.append(word + "ay")
            continue

        # Rule 2: Starts with consonant cluster ending in "qu"
        if "qu" in word:
            qu_index = word.find("qu")
            if qu_index == 0 or (qu_index > 0 and word[qu_index - 1] not in vowels):
                result.append(word[qu_index + 2:] + word[:qu_index + 2] + "ay")
                continue

        # Rule 3: General consonant cluster (including 'y' handling)
        for i, char in enumerate(word):
            if char in vowels or (char == "y" and i != 0):
                result.append(word[i:] + word[:i] + "ay")
                break

    return " ".join(result)