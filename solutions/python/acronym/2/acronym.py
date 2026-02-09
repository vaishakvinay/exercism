import re

def abbreviate(words):

   
    words = words.replace("'", "")

  
    found = re.findall(r"[A-Za-z]+", words)

    acronym = ""

    for word in found:
        acronym += word[0].upper()

    return acronym
