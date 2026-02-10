def is_valid(isbn):
  
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    total = 0

   
    for i, ch in enumerate(isbn):

        
        if ch == 'X':
            if i != 9:        
                return False
            value = 10
        else:
            if not ch.isdigit():
                return False
            value = int(ch)

        weight = 10 - i
        total += value * weight

    return total % 11 == 0
#test
