#!/usr/local/bin/env python3.4
# 2015-7-12

file_in = open('DNA_sequence.fasta','r')

while True:  
    line = file_in.readline()  
    if line:  
        print (line) 

file_in.close()  