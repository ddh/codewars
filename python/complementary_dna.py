def DNA_strand(dna):
    complement = { 'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G' }
    return ''.join([complement[base] for base in dna])