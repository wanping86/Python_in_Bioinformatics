#!/usr/local/bin/env python3.4
# 2015-7-8

dna = 'gatgacgttattaccggactctgtcacgccgcggtgcgagctgaggcgtggcgtctgctggg'

from string import *

def revcomp(dna):
    revcomp = dna.translate(str.maketrans("AGCTagct", "TCGAtcga"))[::-1]
    return revcomp
    
revcomp = revcomp(dna)

print (dna)
print (revcomp)
