def rotate(text, key):
    result = ''
    
    for t in text:
        if t.isupper():
            result += chr((ord(t) - ord('A') + key) % 26 + ord('A'))
        elif t.islower():
            result += chr((ord(t) - ord('a') + key) % 26 + ord('a'))
        else:
            result += t  # Keep spaces and punctuation unchanged
    
    return result
        
        