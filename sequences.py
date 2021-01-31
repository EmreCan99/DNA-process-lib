#1.dosya

def validate_dna(dna_seq):
    seqm = dna_seq.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("T") + seqm.count("G")
    if valid == len(seqm):
        return True
    else:
        return False

def frequency(seq):
    dic ={}
    for s in seq:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    return dic

def gc_content (dna_seq):
    udna_seq = dna_seq.upper()
    gc_count = 0
    for s in udna_seq:
        if s in "GC":
            gc_count += 1
    return gc_count / len(udna_seq)

def gc_content_subseq (dna_seq , k=100):
    res = []
    for i in range(0, len (dna_seq)-k+1, k):
        subseq = dna_seq[i:i+k]
        gc = gc_content(subseq)
        res.append(gc)
    return res

#2.dosya - transkripsiyon

def transcription(dna_seq):
    assert validate_dna(dna_seq), "yamuk veri girdin"
    return dna_seq.upper().replace("T","U")

def reverse_complement(dna_seq):
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    comp = ""
    for c in dna_seq.upper():
        if c == "A":
            comp= "T" + comp
        elif c == "T":
            comp = "A" + comp
        elif c == "G":
            comp = "C" + comp
        elif c== "C":
            comp = "G" + comp
    return comp

#3.dosya - translasyon

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

#4.dosya - reading frames

def reading_frames(dna_seq):
    
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    res = []
    res.append(translate_seq(dna_seq ,0))
    res.append(translate_seq(dna_seq ,1))
    res.append(translate_seq(dna_seq ,2))
    rc = reverse_complement(dna_seq)
    res.append(translate_seq(rc,0))
    res.append(translate_seq(rc,1))
    res.append(translate_seq(rc,2))
    return res

def all_proteins_rf (aa_seq):

    aa_seq = aa_seq.upper()
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else :
            if aa == "M":
                current_prot.append("")
                for i in range( len (current_prot)):
                    current_prot[i] += aa
    return proteins


def all_orfs (dna_seq):
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    rfs = reading_frames (dna_seq)
    res = []
    for rf in rfs:
        prots = all_proteins_rf(rf)
        for p in prots: res.append(p)
    return res

def all_orfs_ord (dna_seq , minsize = 0):
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    rfs = reading_frames (dna_seq)
    res = []
    for rf in rfs:
        prots = all_proteins_rf(rf)
        for p in prots:
            if len(p) > minsize: insert_prot_ord(p, res)
    return res

def insert_prot_ord (prot, list_prots):
    i = 0
    while i < len (list_prots) and len (prot) < len (list_prots[i]):
        i += 1
    list_prots.insert(i, prot)
    


    print(transcription("attcctatctactactatctctcttctcca"))