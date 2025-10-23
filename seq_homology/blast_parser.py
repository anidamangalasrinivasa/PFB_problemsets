#!/usr/bin/env python3
import re,sys

#matrices for BLAST: BLOSUM62 BLOSUM80 PAM30 PAM70
matrices={'BLOSUM62','BLOSUM80','PAM30','PAM70'}
seq_name=sys.argv[1]

#getting filenames for each blast result file

list_of_filenames=[]

for matrix in matrices:
    temp_name='blast_'+seq_name+'_v_qfo_' + matrix+'.txt'
    list_of_filenames.append(temp_name)

#opening all files and getting columns into a dictionary:
#input filename and get a dictionary of field:value

def dict_of_result(filename):

    fields=['query acc.ver', 'subject acc.ver', 'pid', 'alen', 'mismatches', 'gap_opens', 'q.start', 'q. end', 's. start', 's. end', 'evalue', 'bit score']
    this_data={}
    with open(filename,'r') as result:
        for line in result:
            if line[0]=='#':
                continue
            else:
                this_data=dict(zip(fields, line.rstrip().split('\t')))
    return this_data

blast_dict={}

for files in list_of_filenames:
    temp_dict=dict_of_result(files)
    if matrix:=re.search(r'.+_(\w+)',files).group(1):
        if matrix not in blast_dict:
            blast_dict[matrix]={}
    blast_dict[matrix]=temp_dict

print(f'Matrix\t%ID \tALength\tEVal')

for matrix in blast_dict:
    print(f'{matrix:<3}\t{blast_dict[matrix]['pid']:>3}\t{blast_dict[matrix]['alen']:>3}\t{blast_dict[matrix]['evalue']:>3}')
