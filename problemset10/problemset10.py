#!/usr/bin/env python3
import sys
import re

def format_string(dna):
    split_dna=re.sub(r'(\S{60})',r'\1\n', dna, flags=re.IGNORECASE)
    split_lines=split_dna.split('\n')
    for lines in split_lines:
        print(f'{lines}')
        

dna='GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

#format_string(dna)

def format_string_spaces(dna):
    dna_nospace=dna.replace('\n','')
    split_dna_1=re.sub(r'(\S{60})',r'\1\n', dna_nospace, flags=re.IGNORECASE)
    split_lines_1=split_dna_1.split('\n')
    for lines in split_lines_1:
        print(f'{lines}')
        
dna2='''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

#format_string_spaces(dna2)

def input_string_split(dna,length):
    dna_nospace=dna.replace('\n','')
    split_dna_2=re.sub(rf'(.{{,{length}}})',r'\1\n', dna_nospace, flags=re.IGNORECASE)
    split_lines_2=split_dna_2.split('\n')
    for lines in split_lines_2:
        print(f'{lines}')

#input_string_split(dna2,20)   

input_string=sys.argv[1]
input_len=sys.argv[2]

#input_string_split(input_string, input_len)   
# def input_string_split(dna,length):
#     count=0
#     dna_temp=''
#     list_temp=[]

#     dna_nospace=input_string.replace('\n','')
#     length_int=int(input_len)
#     number_of_runs=int(len(dna_nospace)/length_int)+1
#     for numbers in range(number_of_runs):
#         dna_temp=dna_nospace[(length_int*count):(length_int*(count+1))]
#         list_temp.append(dna_temp)
#         count+=1
#     print(list_temp)
#     for lines in list_temp:
#         print(f'{lines}')

#input_string_split(input_string,input_len)

#input file with multiple fastas and output formatted lines in fasta format
def parse_format_fastas(fasta,length):

    seqs={}
    gene_list={}
    seq_temp=''
    gene_id_temp=''

    with open(fasta,'r') as seq:
        for line in seq:
            line=line.rstrip()
            if re.search(r'^>',line):
                seq_temp=''
                gene_id_temp=re.search(r'>(\S+) ',line).group(1)
            if line.isalpha():
                seq_temp+=line
            gene_list[gene_id_temp]=seq_temp
    
    for gene in gene_list:
        dna_nospace=gene_list[gene].replace('\n','')
        split_dna_2=re.sub(rf'(.{{1,{length}}})',r'\1\n', dna_nospace, flags=re.IGNORECASE)
        split_lines_2=split_dna_2.split('\n')
        print(f'>{gene}')
        for lines in split_lines_2:
            print(f'{lines}')

#parse_format_fastas(input_string,input_len)

#%gc content function
def gc_content(dna):
    gc_count=dna.count('G')+dna.count('C')
    gc_cont=(gc_count/len(dna))*100
    return(gc_cont)

#reverse_complemet function
def rev_comp(dna):
    seq_c=dna.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
    seq_c1=seq_c.upper()
    seq_rc=seq_c1[::-1]
    return(seq_rc)
