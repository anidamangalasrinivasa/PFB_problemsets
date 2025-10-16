#!/usr/bin/env python3

gene_list={}
gene_id_temp=''
seq_temp=''

with open('Python_06.fasta','r') as fasta:
    for line in fasta:
        line=line.rstrip()
        if line[0]=='>':
            seq_temp=''
            gene_id_temp=line.replace('>','')
            
        if line.isalpha():
            seq_temp+=line
        gene_list[gene_id_temp]=seq_temp

print(gene_list)
       
        