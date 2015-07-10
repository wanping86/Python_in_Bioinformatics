#!/usr/local/bin/env python3.4
# 2015-7-5

def count_base(dna):
	count_a = dna.count('a')
	count_t = dna.count('t')
	count_c = dna.count('c')
	count_g = dna.count('g')
	return [count_a,count_t,count_c,count_g]
