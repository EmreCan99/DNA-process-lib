from sequences import *


seq = input ("Insert DNA sequence:")
if validate_dna (seq):
    print ("Valid sequence")
    print ("Transcription: ", transcription (seq))
    print ("Reverse complement:", reverse_complement(seq))
    print ("GC content (global):", gc_content(seq))
    print ("Direct translation:" , translate_seq(seq))
    print ("All proteins in ORFs (decreasing size): ", all_orfs_ord(seq))
else : print ("DNA sequence is not valid")



# def read_seq_from_file(filename):
#     with open(filename , "r") as fh:
#         lines = fh.readlines()
#         seq = ""
#         for l in lines:
#             seq += l.replace("\n","")
#     return seq

# def write_seq_to_file(seq, filename):
#     with open(filename , "w") as fh:
#         fh.write(seq)
#     return None

# write_seq_to_file(read_seq_from_file("multiLineText.txt"), "yazı.txt")

'''
fname = input ("Insert input filename:")
seq = read_seq_from_file(fname)
if validate_dna (seq):
    print ("Valid sequence")
    print ("Transcription: ", transcription (seq))
    print ("Reverse complement:", reverse_complement(seq))
    print ("GC content (global):", gc_content(seq))
    print ("Direct translation:" , translate_seq(seq))
    orfs = all_orfs_ord(seq)
    i = 1
    for orf in orfs:
        write_seq_to_file(orf, "orf−"+ s t r (i)+".txt")
        i += 1
else : print ("DNA sequence is not valid")
'''