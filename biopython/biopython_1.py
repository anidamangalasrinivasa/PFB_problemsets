#!/usr/bin/env python3

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
file_path='./'+filename
length_NT=0
length_list={}
total_gc_content=0
gc_content_list={}

with open(filename,'r') as fastafile:
    records=list(SeqIO.parse(file_path, "fasta"))
    print(f'Total number of sequences:{len(records)}')
    total_num_seqs=len(records)
    for record in SeqIO.parse(file_path, "fasta"):
        print(f'Number of nucleotides for {record.id}:{len(record.seq)}')
        length_NT+=len(record.seq)
        length_list[record.id]=len(record.seq)
        gc_content=gc_fraction(record.seq)
        total_gc_content+=gc_content
        gc_content_list[record.id]=gc_content

print(f'Average GC countent={total_gc_content/total_num_seqs:.2%}')
print(f'Average seq length={length_NT/total_num_seqs}')
print(f'Max length:{max(length_list.values())}')
print(f'Max GC content:{max(gc_content_list.values()):.2%}')
print(f'Min length:{min(length_list.values())}')
print(f'Max GC content:{min(gc_content_list.values()):.2%}')
