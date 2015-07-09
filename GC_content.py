#!/usr/local/bin/env python3.4
# 2015-7-5

dna = 'gatgacgttattaccggactctgtcacgccgcggtgcgagctgaggcgtggcgtctgctggg'
print (dna.count('c'))
print (dna.count('g'))
print (len(dna))

GC_content = (dna.count('c') + dna.count('g')) / len(dna) 
print (GC_content)
# 0.6451612903225806

GC_content_float = (dna.count('c') + dna.count('g'))/float(len(dna))
print (GC_content_float)
# 0.6451612903225806

GC_content_100 = (dna.count('c') + dna.count('g'))* 100.0/len(dna)
print (GC_content_100)
# 64.51612903225806

GC_content_100_2 = (dna.count('c') + dna.count('g'))/len(dna)* 100.0
print (GC_content_100_2)
# 64.51612903225806

GC_content_100_2_dicimal = (dna.count('c') + dna.count('g'))/float(len(dna))* 100.0
print ("%.2f" %GC_content_100_2_dicimal)
# 64.52


