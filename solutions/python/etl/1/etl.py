def transform(legacy_data):
    ndict={}
    for score, value in legacy_data.items():
        for letter in value:
            letter=letter.lower()
            ndict[letter] = score
    
    return ndict
