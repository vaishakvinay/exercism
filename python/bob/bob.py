def response(hey_bob):
    
    question = hey_bob.strip()

    if question.isupper() and question.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif question.endswith("?"):
        return "Sure." 
    elif not question:
        return "Fine. Be that way!"
    elif question.isupper():
        return "Whoa, chill out!" 
    else:
        return "Whatever." 