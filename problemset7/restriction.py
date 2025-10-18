#!/usr/bin/env python3
import re
import sys

count=0
restrict={}
enzyme=''
site=''

with open('bionet.txt','r') as bionet:
    for line in bionet:
        if count<10:
            count+=1
            continue
        line=line.rstrip()
        for element in re.finditer(r'(\S+.\S+)\s{2,}(\S+)',line):
            enzyme=element.group(1)
            site=element.group(2)
            restrict[enzyme]=site

enz=sys.argv[1]
fasta=sys.argv[2]
sequence=''

with open(fasta,'r') as seq:
    for line in seq:
        line=line.rstrip()
        if line[0]=='>':
            continue
        else:
            sequence+=line

if enz in restrict.keys():
        cut_site_repl=restrict[enz]
        if '^' in cut_site_repl:
            cut_site=cut_site_repl.replace('^','')
            cut_seq=re.sub(cut_site,cut_site_repl,sequence)
        else:
            cut_site='^'+cut_site_repl+'^'
            cut_seq=re.sub(cut_site_repl, cut_site,sequence)

print(f'Original sequence:\n{seq} Cut sequence:\n{cut_seq}')

cutlist=cut_seq.split('^')
no_fragments=len(cutlist)
cutlist_sorted=sorted(cutlist, key=len, reverse=True)
print(f'Number of fragments: {no_fragments}\nFragments in natural order\n{cutlist}\nFragments in sorted order:\n{cutlist_sorted}')

#key_for_nt={'R':'[AG]','Y':'[CT]','S':'[GC]','W':'[AT]','K':'[GT]','M':'[AC]','B':'[CGT]','D':'[AGT]','H':'[ACT]','V':'[ACG]','N':'[ATCG]'}

