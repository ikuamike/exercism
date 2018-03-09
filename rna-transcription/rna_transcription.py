def to_rna(dna_strand):
    DNA = 'GCTA'
    RNA = 'CGAU'
    for i in dna_strand:
        if i not in DNA:
            raise ValueError("Invalid DNA strand")    
    transcription = str.maketrans(DNA, RNA)
    return dna_strand.translate(transcription)
