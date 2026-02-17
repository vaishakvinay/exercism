def response(hey_bob):

    text = hey_bob.strip()

   
    if not text:
        return "Fine. Be that way!"

    
    if text.isupper() and any(c.isalpha() for c in text) and text.endswith('?'):
        return "Calm down, I know what I'm doing!"

    elif text.endswith('?'):
        return "Sure."

    
    elif text.isupper() and any(c.isalpha() for c in text):
        return "Whoa, chill out!"

    else:
        return "Whatever."
