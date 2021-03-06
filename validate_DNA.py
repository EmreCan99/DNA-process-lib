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