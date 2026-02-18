import math

def cipher_text(plain_text):
    
  
    normalized = ""

    for ch in plain_text.lower():
        if ch.isalnum():
            normalized += ch

    
    length = len(normalized)

    if length == 0:
        return ""

   
    cols = math.ceil(math.sqrt(length))
    rows = math.ceil(length / cols)

    
    grid = []

    for i in range(0, length, cols):
        grid.append(normalized[i:i+cols])

  
    result = []

    for c in range(cols):

        word = ""

        for r in grid:
            if c < len(r):
                word += r[c]
            else:
                word += " "
                
        result.append(word)

    
    return " ".join(result)
