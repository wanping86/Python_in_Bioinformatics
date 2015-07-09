#!/usr/local/bin/env python3.4
# 2015-7-9

cdna = 'gatgacgttattaccggactctgtcacgccgcggtgcgagctgaggcgtggcgtctgctggg'

from string import *

standard = { 'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
             'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
             'tta': 'L', 'tca': 'S', 'taa': '*' , 'tca': '*',
             'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tcg': 'W',
             'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
             'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
             'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
             'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
             'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
             'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
             'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
             'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
             'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
             'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
             'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
             'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
}

def dna_translate(cdna, code=standard):
    """ translate a cDNA sequence to a protein """
    prot = ""
    for i in range(0,len(cdna),3):
        prot += code.get(cdna[i:i+3], "?")
    return prot

def dna_translate2(cdna, code=standard):
    """ translate a cDNA sequence to a protein """
    return "".join([ code.get(cdna[i:i+3], "?")
        for i in range(0,len(cdna),3)])

protein = dna_translate(cdna)
print (protein)

protein2 = dna_translate2(cdna)
print (protein2)