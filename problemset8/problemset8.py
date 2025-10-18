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

#NT counts multiD df
for gene in gene_list:
    seqs[gene]={}
    unique_nt=set(gene_list[gene])
    for nt in unique_nt:
        gc_count=gene_list[gene].count(nt)
        seqs[gene][nt]=gc_count
        
for gene in seqs:
    for nt in unique_nt:
        print(f'{seqs[gene]}\t{seqs[gene]['A']}\t{seqs[gene]['T']}\t{seqs[gene]['C']}\t{seqs[gene]['G']}')

#codon
for gene in gene_list:
    codons=re.findall(r'(.{3})',gene_list[gene])
    print(f'{gene}-frame1-codons')
    for codon in codons:
        print(f'{codon}',end='\t')
    print()

#reading frames
for gene in gene_list:
    for start in range(3):
        gene_seq=gene_list[gene]
        codons=re.findall(r'(.{,3})',gene_seq[start:])
        print(f'{gene}-frame {start}-codons')
        for codon in codons:
            print(f'{codon}',end='\t')
        print()
    print()

#all 6 reading frames

for gene in gene_list:
    for start in range(3):
        gene_seq=gene_list[gene]
        seq_c=gene_seq.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
        seq_c1=seq_c.upper()
        seq_rc=seq_c1[::-1]
        codons=sorted(re.findall(r'(.{,3})',gene_seq[start:]))
        print(f'{gene}-frame {start+1}-codons')
        for codon in codons:
            print(f'{codon}',end='\t')
        print()
        re_codons=sorted(re.findall(r'(.{,3})',seq_rc[start:]))
        print(f'RC {gene}-frame {start+1}-codons')
        for codon in re_codons:
            print(f'{codon}',end='\t')
        print()
    print()

#writing to file:
with open('Python_08.codons-6frames.nt','w') as nt1:
    for gene in gene_list:
        for start in range(3):
            gene_seq=gene_list[gene]
            seq_c=gene_seq.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
            seq_c1=seq_c.upper()
            seq_rc=seq_c1[::-1]
            codons=sorted(re.findall(r'(.{,3})',gene_seq[start:]))
            nt1.write(f'{gene}-frame {start+1}-codons\n')
            for codon in codons:
                nt1.write(f'{codon}\t')
            nt1.write('\n')
            re_codons=sorted(re.findall(r'(.{,3})',seq_rc[start:]))
            nt1.write(f'RC {gene}-frame {start+1}-codons')
            for codon in re_codons:
                nt1.write(f'{codon}\t')
            nt1.write('\n')
        nt1.write('\n')

#translation
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
orfs=[]

for gene in gene_list:
    for start in range(3):
        gene_seq=gene_list[gene]
        seq_c=gene_seq.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
        seq_c1=seq_c.upper()
        seq_rc=seq_c1[::-1]
        codons=sorted(re.findall(r'(.{,3})',gene_seq[start:]))
        print(f'Translation for {gene}-frame {start+1}')
        for codon in codons:
            if codon in translation_table.keys():
                amino=translation_table[codon]
                orfs+=amino
                print(f'{amino}',end='\t')
        print()
        re_codons=sorted(re.findall(r'(.{,3})',seq_rc[start:]))
        print(f'Translation for RC {gene}-frame {start+1}')
        for codon in re_codons:
            if codon in translation_table.keys():
                amino=translation_table[codon]
                orfs+=amino
                print(f'{amino}',end='\t')
        print()
    print()

    