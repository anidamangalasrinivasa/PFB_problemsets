#!/usr/bin/env python3
import sys
import re

input=sys.argv[1]
seqs={}
gene_list={}
seq_temp=''
gene_id_temp=''
orfs=[]

with open(input,'r') as seq:
    for line in seq:
        line=line.rstrip()
        if re.search(r'^>',line):
            seq_temp=''
            gene_id_temp=re.search(r'>(\S+) ',line).group(1)
        if line.isalpha():
            seq_temp+=line
        gene_list[gene_id_temp]=seq_temp

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

with open('Python_08.codons-6frames.nt','w') as codons, open('Python_08.translated.aa','w') as translated, open('Python_08.translated-longest.aa','w') as longest:
    for gene in gene_list:
        for start in range(3):
            gene_seq=gene_list[gene]
            seq_c=gene_seq.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
            seq_c1=seq_c.upper()
            seq_rc=seq_c1[::-1]
            codons=re.findall(r'(.{,3})',gene_seq[start:])
            translated.write(f'Translation for {gene}-frame {start+1}\n')
            codons.write(f'{gene}-frame {start+1}-codons\n')
            for codon in codons:
                codons.write(f'{codon}\t')
                if codon in translation_table.keys():
                    amino=translation_table[codon]
                    translated.write(amino)
            translated.write('\n')
            re_codons=re.findall(r'(.{,3})',seq_rc[start:])
            translated.write(f'Translation for RC {gene}-frame {start+1}\n')
            for codon in re_codons:
                codons.write(f'{codon}\t')
                if codon in translation_table.keys():
                    amino=translation_table[codon]
                    translated.write(amino)
            translated.write('\n')
        translated.write('\n')

