#!/usr/bin/env python

import os, sys, math

from sequence_to_kmer_list import *
from fastq_to_file_sequence_list import *


## method: count_kmers(kmer_list)
##
##  Counts the frequency of each kmer in the given list of kmers
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##
##
##  returns kmer_counts_dict : dict containing ( kmer : count )
##                    ie.  {  "GATC" : 2,
##                            "TCGA" : 1,
##                             ...       }

def shannon_entropy(kmer):
    kmer_probs={}
    probs=[]
    nts=set(kmer)
    for nt in nts:
        kmer_probs[nt]=kmer.count(nt)/len(kmer)
    for key in kmer_probs.keys():
        if kmer_probs[key]>0:
            probs.append(kmer_probs[key]*(math.log2(kmer_probs[key])))
    
    entropy=-(sum(probs))
    return entropy



def count_kmers(kmer_list):

    kmer_count_dict = dict()
    ##################
    ## Step 2:
    ## begin your code
    for kmer in kmer_list:
        if kmer not in kmer_count_dict.keys():
            kmer_count_dict[kmer]=1
        else:
            kmer_count_dict[kmer]+=1
    ## end your code
    ################

    return kmer_count_dict


def main():

    progname = sys.argv[0]

    usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(
        progname
    )

    if len(sys.argv) < 4:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    kmer_length = int(sys.argv[2])
    num_top_kmers_show = int(sys.argv[3])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    all_kmers = list()

    #######################
    ## Step 1:
    ## begin your code, populate 'all_kmers' list with the
    ## collection of kmers from all sequences
    for sequence in seq_list:
        temp_seq_list=sequence_to_kmer_list(sequence,kmer_length)
        all_kmers.extend(temp_seq_list)
    ## end your code
    #######################

    kmer_count_dict = count_kmers(all_kmers)  # see step 2 above. You implement this. :-)
    
    #########################
    ## Step 3: sort unique_kmers by abundance descendingly
    ## (Note, you can run and test without first implementing Step 3)
    ## begin your code       hint: see the built-in 'sorted' method documentation
    kmer_count_dict=dict(sorted(kmer_count_dict.items() ,key=lambda kmers_tuple: kmers_tuple[1], reverse=True))
    
    ## end your code
    # unique_kmers = list(kmer_count_dict.keys())
    ## getting the num top kmers to show
    top_kmers_show = list(kmer_count_dict.keys())[0:num_top_kmers_show]

    for kmer in top_kmers_show:
    
        print(f"{kmer}: {kmer_count_dict[kmer]}\t{shannon_entropy(kmer):.2f}")

    sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == "__main__":
    main()