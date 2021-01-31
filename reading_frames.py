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
    while i < len (list_prots) and l en (prot) < len (list_prots[i]):
        i += 1
    list_prots.insert(i, prot)
    