def translate(text):

    result = []
    vowels = ["a","e","i","o","u"]

    words = text.split()

    for word in words:

       
        if word[0] in vowels or word[0:2] == "xr" or word[0:2] == "yt":
            result.append(word + "ay")

        else:
            for i, ch in enumerate(word):

              
                if word[i:i+2] == "qu":
                    result.append(word[i+2:] + word[:i+2] + "ay")
                    break

              
                if ch in vowels or (ch == "y" and i != 0):
                    result.append(word[i:] + word[:i] + "ay")
                    break

    return " ".join(result)
