#!/usr/bin/env python3
import sys
import re

input=sys.argv[1]
seqs={}
gene_list={}
seq_temp=''
gene_id_temp=''

with open(input,'r') as seq:
    for line in seq:
        line=line.rstrip()
        if re.search(r'^>',line):
            seq_temp=''
            gene_id_temp=re.search(r'>(\S+) ',line).group(1)
        if line.isalpha():
            seq_temp+=line
        gene_list[gene_id_temp]=seq_temp

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

orfs={}
orfs_rev={}

with open('Python_08.codons-6frames.nt','w') as cods, open('Python_08.translated.aa','w') as translated:
    for gene in gene_list:
        for start in range(3):
            gene_seq=gene_list[gene]
            AA_seq=''
            AA_seq_rev=''
            seq_c=gene_seq.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
            seq_c1=seq_c.upper()
            seq_rc=seq_c1[::-1]
            codons=re.findall(r'(.{,3})',gene_seq[start:])
            translated.write(f'Translation for {gene}-frame {start+1}\n') #writing translation heading
            cods.write(f'{gene}-frame {start+1}-codons\n') #writing codons heading
            for codon in codons:
                cods.write(f'{codon}-') #writing codons to codon file
                if gene not in orfs.keys():
                    orfs[gene]={}
                if start+1 not in orfs[gene]:
                    orfs[gene][start+1]={}
                if codon in translation_table.keys():
                    amino=translation_table[codon]
                    translated.write(amino) #writing amino acid to translated file WITHOUT space
                    AA_seq+=amino
                    orfs[gene][start+1]=AA_seq
            translated.write('\n')
            cods.write('\n') #adding a new line to translation after all forward codons were translated
            re_codons=re.findall(r'(.{,3})',seq_rc[start:])
            translated.write(f'Translation for RC {gene}-frame {start+1}\n') #writing to translation file
            cods.write(f'RC {gene}-frame {start+1}-codons\n') #writing to codon file
            for codon in re_codons:
                cods.write(f'{codon}-') #writing reverse codon to codon file
                if start+4 not in orfs[gene]:
                    orfs[gene][start+4]={}
                if codon in translation_table.keys():
                    amino=translation_table[codon]
                    AA_seq_rev+=amino
                    orfs[gene][start+4]=AA_seq_rev
                    translated.write(amino) #adding reverse codon AA to translated file without space
            cods.write('\n')
            translated.write('\n')
        cods.write('\n')
        translated.write('\n')

#Finding longest ORF
orf_collection={}
longest_orf={}

for genes in orfs.keys():
    if genes not in orf_collection.keys():
            orf_collection[genes]={}
    for key1 in range(1,7):
        if key1 not in orf_collection[genes]:
            orf_collection[genes][key1]=[]
        query=orfs[genes][key1]
        orf_seq=re.findall(r'(M.+?\*)', query)
        orf_collection[genes][key1]+=orf_seq

#print(orf_collection)
    
for genes in orf_collection:
    if genes not in longest_orf.keys():
        longest_orf[genes]={}
    for key1 in range(1,7):
        if key1 not in longest_orf[genes]:
            longest_orf[genes][key1]=''
        query2=orf_collection[genes][key1]
        if query2:
            maxi_len=max(query2,key=len)
            longest_orf[genes][key1]=maxi_len
        
#print(longest_orf)

#writing this to a file:

with open('Python_08.translated-longest.aa','w') as lo_write:
    for genes in longest_orf:
        lo_write.write(f'Longest ORF for each translation frame in gene {genes}\n')
        for keys in range(1,7):
            string1=longest_orf[genes][keys]
            lo_write.write(f'Translation frame: {keys}\n >{genes}\n{string1}\n')
