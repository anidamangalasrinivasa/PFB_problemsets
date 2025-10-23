#!/usr/bin/env python3
import re,sys
from blast_parser import dict_of_result

matrices={'BL50','BL62','VT10',' VT20','VT40','VT80',' VT160'}
seq_name=sys.argv[1]

#getting filenames for each blast result file

list_of_filenames=[]

for matrix in matrices:
    temp_name='ss_'+seq_name+'_v_qfo_' + matrix+'.txt'
    list_of_filenames.append(temp_name)


blast_dict={}

for files in list_of_filenames:
    temp_dict=dict_of_result(files)
    if matrix:=re.search(r'.+_(\w+)',files).group(1):
        if matrix not in blast_dict:
            blast_dict[matrix]={}
    blast_dict[matrix]=temp_dict


print(f'Matrix\tPercentage ID\tALength\tEVal')

for matrix in blast_dict:
    print(f'{matrix:<3}\t{blast_dict[matrix]['pid']:>3}\t{blast_dict[matrix]['alen']:>3}\t{blast_dict[matrix]['evalue']:>3}')
