#!/usr/bin/env python3
import random as rand
original_seq='GAATCGGCCAA'
seq_list=list(original_seq)
length=len(seq_list)

for n in original_seq:
    ind_1=rand.randrange(0,(length))
    ind_2=rand.randrange(0,(length))
    if ind_1!=ind_2:
        seq_list[ind_1],seq_list[ind_2]=seq_list[ind_2],seq_list[ind_1]
    print(f'Indices shuffled for this round:{ind_1} and {ind_2}')
print(f'Final sequence:{''.join(seq_list)}')

   




