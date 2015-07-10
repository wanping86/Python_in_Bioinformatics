#!/usr/local/bin/env python3.4
# 2015-7-10

dna = 'gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctggg'

def count_base(dna):
	count_a = dna.count('a')
	count_t = dna.count('t')
	count_c = dna.count('c')
	count_g = dna.count('g')
	return [count_a,count_t,count_c,count_g]

base_count = count_base(dna)

print ('A\t',base_count[0])
print ('T\t',base_count[1])
print ('C\t',base_count[2])
print ('G\t',base_count[3])
