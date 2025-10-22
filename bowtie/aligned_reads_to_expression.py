#!/usr/bin/env python3
import re, sys

filename=sys.argv[1]

bam_dict={}

with open(filename,'r') as sam:
    for line in sam:
        line.rstrip()
        temp_comps=line.split('\t')
        if gene_id:=re.search(r'^[^\^]+',temp_comps[2]).group(0):
            if gene_id not in bam_dict:
                bam_dict[gene_id]=[]
            bam_dict[gene_id].append(temp_comps[0])

count_dict={}

for gene_id in bam_dict.keys():
    set_list_count=0
    set_list_count=len(list(set(bam_dict[gene_id])))
    count_dict[gene_id]=set_list_count


count_dict=dict(sorted(count_dict.items() ,key=lambda kmers_tuple: kmers_tuple[1], reverse=True))

for gene_id in count_dict.keys():
    print(f'{gene_id}:{count_dict[gene_id]}')