class MySeq:
""" Class for biological sequences. """
    def __init__ ( self, seq, seq_type = "DNA"):
        selfseq = seq.upper()
        self.seq_type = seq_type
    def __len__( self):
        return len( self.seq)
    def __getitem__( self, n):
        return self.seq[n]
    def __getslice__( self i, j):
        return self.seq[i:j]
    def __str__( self):
        return self.seq
    def get_seq_biotype ( self):
        return self.seq_type
    def show_info_seq ( self):
        print ("Sequence: " + self.seq + " biotype: " + self.seq_type)

    def alphabet (self):
        if ( self.seq_type=="DNA"): return "ACGT"
        elif ( self.seq_type=="RNA"): return "ACGU"
        elif ( self.seq_type=="PROTEIN"): return "ACDEFGHIKLMNPQRSTVWY"
        else : return None
    def validate ( self):
        alp = self.alphabet()
        res = True
        i = 0
        while i < len ( self.seq) and res:
            if self .seq[i] not in alp: res = False
            else: i += 1
        return res

    def transcription ( self):
        if ( self.seq_type == "DNA"):
            return MySeq( self .seq.replace("T","U"), "RNA")
        else :
            return None
    def reverse_comp ( self):
        if ( self .seq_type != "DNA"): return None
        comp = ""
        for c in self.seq:
            if (c == 'A'): comp = "T" + comp
            elif (c == "T"): comp = "A" + comp
            elif (c == "G"): comp = "C" + comp
            elif (c== "C"): comp = "G" + comp
        return MySeq(comp, "DNA")

    def translate ( self, iniPos= 0):
        if ( self.seq_type != "DNA"): return None
        seq_aa = ""
        for pos in range(iniPos , len ( self.seq)−2,3):
            cod = self.seq[pos:pos+3]
            seq_aa += translate_codon(cod)
        return MySeq(seq_aa , "PROTEIN")

        