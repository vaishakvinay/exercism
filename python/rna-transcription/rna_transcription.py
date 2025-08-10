def to_rna(dna_strand):
    
    
    if dna_strand == '':
        raise ValueError("DNA strand cannot be empty")
    
def to_rna(dna_strand):
    rna_strand = ''
    for d in dna_strand:
        if d == 'G':
            rna_strand += 'C'
        elif d == 'C':
            rna_strand += 'G'
        elif d == 'T':
            rna_strand += 'A'
        elif d == 'A':
            rna_strand += 'U'
        else:
            raise ValueError(f"Invalid nucleotide: {d}")
    return rna_strand  
