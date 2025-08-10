def is_valid(isbn):
    
    clean = isbn.replace("-", "").replace(" ", "")


    if len(clean) != 10:
        return False    
    
    total=0
    for i,ch in enumerate(clean):
        if i == 9 and ch == 'X':
            digit = 10
        elif ch.isdigit():
            digit = int(ch)
        else:
            return False     
        
        total += digit * (10 - i)

    return total % 11 == 0
