#!/usr/bin/env python3
import Bio.Seq
from Bio.Seq import Seq
from Bio import SeqIO
import re
import argparse
from Bio.SeqUtils import gc_fraction

parser = argparse.ArgumentParser(
    description=("Enter a fasta sequnece"))

parser.add_argument("file", help="path to or fasta file name")

args = parser.parse_args()

filename=args.file
#file_path='/Users/pfb/BLAST_analysis'+filename

seq_desc_mod={}
s_paratyphi_b={}

with open(filename,'r') as fastafile:
    for records in SeqIO.parse(filename,"fasta"):
        seq_desc=re.finditer(r'OS=(\w+\s\w+)\s)'.group(1),records.description)
        seq_desc_mod[records.id]=seq_desc
        s_paratyphi_b[records.id]=[]
        for seqs in re.finditer(r'Salmonella paratyphi B', records.description):
            (s_paratyphi_b[records.id]).append(seqs)

print(f'{s_paratyphi_b[0:5]}')
print(f'{seq_desc_mod[0:5]}')
            



    