def is_isogram(string):
    
    text = string.replace(" ", "").replace("-", "").lower()

    seen = []

    for ch in text:
        if ch in seen:
            return False
        seen.append(ch)

    return True
    