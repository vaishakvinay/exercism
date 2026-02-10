def rotate(text, key):
    
    new = ""

    for ch in text:

      
        if 'a' <= ch <= 'z':
            new += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))

        elif 'A' <= ch <= 'Z':
            new += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))

        # non-letters stay same
        else:
            new += ch

    return new