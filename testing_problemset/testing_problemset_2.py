#!/usr/bin/env python3
import pytest

def reverse_complement(dna):
    valid = {'A', 'C', 'G', 'T', 'N'}
    seq_upper=dna.upper()
    if not set(seq_upper).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    if len(dna) == 0:
        return 0
    seq_c=seq_upper.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
    seq_c1=seq_c.upper()
    seq_rc=seq_c1[::-1]
    return seq_rc

def test_all_lower_reverse_complent():
    expected='TGCA'
    observed=reverse_complement('tgca')
    assert observed==expected, f'{expected}={observed}'

def test_all_upper_reverse_complement():
    expected='TGCA'
    observed=reverse_complement('TGCA')
    assert observed==expected, f'{expected}={observed}'

def test_mixed_reverse_complement():
    expected='TGCA'
    observed=reverse_complement('tGcA')
    assert observed==expected, f'{expected}={observed}'

def test_wrong_input_reverse_complement():
    try:
        observed=reverse_complement('XYATN')
    except ValueError:
        return
    assert False,'expected ValueError'
    
   
