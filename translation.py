def translate_codon(cod): 
    tc = {"GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "TGT":"C", "TGC":"C",
    "GAT":"D", "GAC":"D",
    "GAA":"E", "GAG":"E",
    "TTT":"F", "TTC":"F",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",
    "CAT":"H", "CAC":"H",
    "ATA":"I", "ATT":"I", "ATC":"I",
    "AAA":"K", "AAG":"K",
    "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "ATG":"M", "AAT":"N", "AAC":"N",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
    "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "TGG":"W",
    "TAT":"Y", "TAC":"Y",
    "TAA":"_", "TAG":"_", "TGA":"_"}
    if cod in tc:
        return tc[cod]
    else:
        return None

def translate_seq (dna_seq , ini_pos = 0):
    """ Translates a DNA sequence into an aminoacid sequence. """
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    seqm = dna_seq.upper()
    seq_aa = ""
    for pos in range(ini_pos , len (seqm)-2,3):
        cod = seqm[pos:pos+3]
        seq_aa += translate_codon(cod)
    return seq_aa
