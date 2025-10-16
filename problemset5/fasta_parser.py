#!/usr/bin/env python3
gene_list={}

with open('Python_06.fasta','r') as fasta, open ('Python_06_nolines.fasta','w') as fasta_nolines:
    for line in fasta:
        no_lines=line.replace('\n','')
        fasta_nolines.write(no_lines)

with open('Python_06_nolines.fasta','r') as fasta, open('Python_06_newlines.fasta','w') as fasta_nl:
    for line in fasta:
        new_lines=line.replace('>','\n').replace('1','1 ').replace('2','2 ').replace('3','3 ').replace('4','4 ')
        fasta_nl.write(new_lines)
    
with open('Python_06_newlines.fasta','r') as fasta:
    for line in fasta:
        line=line.rstrip()
        if line=='':
            continue
        gene_id,seq=line.split()
        gene_list[gene_id]=seq
        #print(parts)

print(gene_list)