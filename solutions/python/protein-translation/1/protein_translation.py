def proteins(strand):
    ndict = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }

    
    result = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]  # slice 3 letters at a time
        amino_acid = ndict.get(codon)
        if amino_acid == "STOP":
            break
        if amino_acid:
            result.append(amino_acid)
    return result
