#!/usr/bin/env python3
import re

#Problem 1
lines_comp=''

with open('Python_07_nobody.txt','r') as python7:
    for line in python7:
        lines_comp+=line
    for found in re.finditer(r'Nobody', lines_comp):
        print(f'\'Nobody\' Found at {found.start(0)+1}')

with open('Bob.txt','w') as bob:
    no_nobody=re.sub(r'Nobody',r'Bob',lines_comp)
    for line in no_nobody:
        bob.write(f'{line}')


#Problem 3
seq_ids=[]
with open('Python_07.fasta','r') as fasta:
        for line in fasta:
            seq_ids+=re.findall(r'>\S+',line)
        print(seq_ids)


#Problem 4
with open('Python_07.fasta','r') as fasta:
     for line in fasta:
          for found in re.finditer(r'>(\S+) (.+)\n',line):
               print(f'ID: {found.group(1)}\tDescription: {found.group(2)}')

#Problem 5: FASTA parser with re
gene_list={}
gene_id=''
seq=''

with open('Python_07.fasta','r') as fasta:
     for line in fasta:
        if re.search(r'>(\S+) (.+)\n',line):
            seq_temp=''
            gene_id+=re.search(r'>(\S+) (.+)\n',line).group(1)
        else:
            line=line.rstrip()
            seq_temp+=line
        gene_list[gene_id]=seq_temp
print(gene_list)
        
#Problem 6:
apoI_list={}
apoI_id=''
apoI_seq=''

with open('Python_07_ApoI.fasta','r') as apoI:
    for line in apoI:
        if re.search(r'>(\S+)\n',line):
            apoI_seq=''
            apoI_id+=re.search(r'>(\S+)\n',line).group(1)
        else:
            line=line.rstrip()
            apoI_seq+=line
        apoI_list[apoI_id]=apoI_seq

print(apoI_list)

print(f'{re.findall(r'[AG]AAT[CT]',apoI_list['seq1'])}')

#problem 7
if re.findall(r'[AG]AAT[CT]',apoI_list['seq1']):
    print(f'cut sequence: {re.sub(r'([AG])AAT([CT])',r'\1^AAT\2',apoI_list['seq1'])}')

#problem 8

cutlist=apoI_list['seq1'].split('^')
cutlist_sort=sorted(cutlist, key=len, reverse=True)
for fragment in cutlist_sort:
    print(fragment)

