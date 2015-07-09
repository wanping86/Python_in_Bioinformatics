#!/usr/local/bin/env python3.4
# 2015-7-6

dna = 'gatgacgttattaccggactctgtcacgccgcggtgcgagctgaggcgtggcgtctgctggg'

trans = str.maketrans("ATCGatcg", "TAGCtagc")

complememtary_DNA = dna.translate(trans)

print (dna)
print (complememtary_DNA)
