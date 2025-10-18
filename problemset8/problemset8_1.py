#!/usr/bin/env python3
import sys
import re

input=sys.argv[1]
seqs={}
gene_list={}
seq_temp=''
gene_id_temp=''

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

with open('Python_08.translated.aa','w') as nt1:
    for gene in gene_list:
        for start in range(3):
            gene_seq=gene_list[gene]
            seq_c=gene_seq.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
            seq_c1=seq_c.upper()
            seq_rc=seq_c1[::-1]
            codons=re.findall(r'(.{,3})',gene_seq[start:])
            nt1.write(f'Translation for {gene}-frame {start+1}\n')
            for codon in codons:
                if codon in translation_table.keys():
                    amino=translation_table[codon]
                    nt1.write(amino)
            nt1.write('\n')
            re_codons=re.findall(r'(.{,3})',seq_rc[start:])
            nt1.write(f'Translation for RC {gene}-frame {start+1}\n')
            for codon in re_codons:
                if codon in translation_table.keys():
                    amino=translation_table[codon]
                    nt1.write(amino)
            nt1.write('\n')
        nt1.write('\n')

orfs=[]
seq_temp=''

with open('Python_08.translated.aa','r') as translated:
    for line in translated:
        line=line.rstrip()
        if re.search('^Tra',line):
            seq_temp=''
            continue
        else:
            seq_temp+=line
        orfs.append(seq_temp)



