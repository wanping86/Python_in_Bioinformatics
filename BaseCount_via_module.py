#!/usr/local/bin/env python3.4
# 2015-7-10

import BaseCount_def

dna = 'gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctggg'
base_count = BaseCount_def.count_base(dna)

print ('A\t',base_count[0])
print ('T\t',base_count[1])
print ('C\t',base_count[2])
print ('G\t',base_count[3])