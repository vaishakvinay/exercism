def answer(question):

    
    if not question.startswith("What is"):
        raise ValueError("syntax error")

   
    text = question.replace("What is ", "").replace("?", "")
    tokens = text.split()

    
    if not tokens:
        raise ValueError("syntax error")


    if not tokens[0].lstrip('-').isdigit():
        raise ValueError("syntax error")

    
    result = int(tokens[0])
    i = 1

    
    while i < len(tokens):

        op = tokens[i]

        
        if op == "plus":
            if i+1 >= len(tokens) or not tokens[i+1].lstrip('-').isdigit():
                raise ValueError("syntax error")

            result += int(tokens[i+1])
            i += 2

        
        elif op == "minus":
            if i+1 >= len(tokens) or not tokens[i+1].lstrip('-').isdigit():
                raise ValueError("syntax error")

            result -= int(tokens[i+1])
            i += 2

       
        elif op == "multiplied":
            if (
                i+2 >= len(tokens)
                or tokens[i+1] != "by"
                or not tokens[i+2].lstrip('-').isdigit()
            ):
                raise ValueError("syntax error")

            result *= int(tokens[i+2])
            i += 3

        
        elif op == "divided":
            if (
                i+2 >= len(tokens)
                or tokens[i+1] != "by"
                or not tokens[i+2].lstrip('-').isdigit()
            ):
                raise ValueError("syntax error")

            result //= int(tokens[i+2])
            i += 3

        
        elif op.lstrip('-').isdigit():
            raise ValueError("syntax error")

        
        else:
            raise ValueError("unknown operation")

    return result

