#!/usr/bin/env python3
import re, sys

filename=sys.argv[1]

bam_dict={}

with open(filename,'r') as sam:
    for line in sam:
        line.rstrip()
        temp_comps=line.split('\t')
        print(temp_comps)
        break