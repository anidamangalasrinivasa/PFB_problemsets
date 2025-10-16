#!/usr/bin/env python3

nt_count={}

with open('Python_06.seq.txt','r') as seq_list:
    for line in seq_list:
        nt_count={}
        line=line.rstrip()
        gene_names,seqs=line.split(sep='\t')
        unique_nt=set(seqs)
        for nt in unique_nt:
            count=seqs.count(nt)
            nt_count[nt]=count
        gc_count=nt_count['G']+nt_count['C']
        total_NT=len(seqs)
        print(f'Name of sequence:{gene_names} Count of nucleotides: {nt_count} GC content: {gc_count/total_NT:.0%}')