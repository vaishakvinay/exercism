def encode(plain_text):


  
    plain_text = plain_text.lower()
    
    encoded = ""


    for ch in plain_text:
        
       
        if 'a' <= ch <= 'z':
            mirrored = chr(ord('z') - (ord(ch) - ord('a')))
            encoded += mirrored
        
    
        elif ch.isdigit():
            encoded += ch
        

        else:
            continue


    grouped = ""
    
    for i in range(0, len(encoded), 5):
        grouped += encoded[i:i+5] + " "

    return grouped.strip()


def decode(ciphered_text):
    

    
    ciphered_text = ciphered_text.replace(" ", "")

    decoded = ""

    for ch in ciphered_text:

        if 'a' <= ch <= 'z':
            mirrored = chr(ord('z') - (ord(ch) - ord('a')))
            decoded += mirrored

        elif ch.isdigit():
            decoded += ch

    return decoded

