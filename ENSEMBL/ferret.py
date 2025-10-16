#!/usr/bin/env python3

with open('ferret_all_genes.tsv','r') as allg, open('ferret_stemcellproliferation_genes.tsv', 'r') as scp, open('ferret_pigmentation_genes.tsv','r') as pig:
    set_all=set(allg)
    set_SCP=set(scp)
    set_pig=set(pig)

set_not_prolif=set_all-set_SCP
set_prolif_pig=set_SCP&set_pig


with open('ferret_transcription_factors.tsv','r') as trans, open('ferret_stemcellproliferation_genes.tsv', 'r') as scp:
    set_trans=set(trans)
    set_scp=set(scp)

set_trans_and_scp=set_trans&set_scp
