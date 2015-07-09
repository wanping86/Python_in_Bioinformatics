#!/usr/local/bin/env python3.4
# 2015-7-9

dna = 'gagaattctgacgttattaccggagaattcctctgtcacgccgcggtgcgagctgaggcgtggcgtctgctggg'
EcoRI = 'gaattc'

from string import *

def restrict(dna, enz):
    "print all start positions of a restriction site"
    site = dna.find(enz)
    while site != -1:
        print ("restriction site %s at position %d" % (enz, site))
        site = dna.find (enz, site + 1)

restrict(dna, EcoRI)