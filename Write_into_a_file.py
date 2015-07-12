#!/usr/local/bin/env python3.4
# 2015-7-12

file_input = open('DNA_sequence.fasta','r')

import sys
output = sys.stdout
file_output = open('DNA_sequence_outputfile.fasta','w')
sys.stdout = file_output

while True:  
    line = file_input.readline()  
    if line:  
        file_output.writelines(line)
    else:  
        break

file_input.close()  
file_output.close()

sys.stdout = output