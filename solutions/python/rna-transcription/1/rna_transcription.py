rna={"G" : "C",
     "C" : "G",
     "T" : "A",
     "A" : "U"}


def to_rna(dna_strand):

    new=''
    
    for ch in dna_strand:
        new+=rna[ch]

    return new
