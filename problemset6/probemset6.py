#!/usr/bin/env python3

#problem1+2

with open('Python_06.txt','r') as seq_read, open('Python_06_uc.txt','w') as seq_write:
    for line in seq_read:
        line=line.rstrip()
        seq_write.write(f'{line.upper()}\n')
        print(f'{line.upper()}')
print(f'It\'s done!')

#problem3
#read sequence file, extract sequences and find RC and output fasta format sequences

seqs=[]
gene_names=[]

with open('Python_06.seq.txt','r') as seq_list:
    for line in seq_list:
        line=line.rstrip()
        gene_names,seqs=line.split(sep='\t')
        seq_c=seqs.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
        seq_c1=seq_c.upper()
        seq_rc=seq_c1[::-1]
        print(f'>{gene_names} Reverse complement:\t{seq_rc}\n')

#problem4

#total number of lines
count_line=0

#total number of characters
count_char=0

#total number of nucleotides+quality characters
length_NT=0

#total number of nucleotides+quality LINES
count_NT=0

with open('Python_06.fastq','r') as fastq:
    for line in fastq:
        line=line.rstrip()
        count_char+=len(line) #gives you total number of characters
        count_line+=1 #gives you total number of lines
        if count_line%2==0: #gives even numbered lines, which are NT sequences and the quality
            count_NT+=1 #adds a line number for each NT or quality line
            length_NT+=len(line) #adds characters for each NT or quality line
    

avg_length=count_char/count_line
avg_seq_length=length_NT/count_NT
count_seq_ID=count_line/4


print(f'total number of seq IDs: {count_seq_ID},Average length of all seqs: {avg_length},Total number of nucleotide lines: {count_NT/2},Total number of NTs:{length_NT/2},Average NT line length:{avg_seq_length}')   
        
        


