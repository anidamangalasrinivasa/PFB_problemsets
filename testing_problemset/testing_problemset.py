#!/usr/bin/env python3
import pytest

def gc_content(seq):
    valid = {'A', 'C', 'G', 'T', 'N'}
    seq1=seq.upper()
    if not set(seq1).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    if len(seq1) == 0:
        return 0
    return (seq1.count('G') + seq1.count('C')) / len(seq1)

def test_gcgc_gc_content():
    expected=1.0
    observed=gc_content('GCGC')
    assert observed==expected, f'worked-expected output {expected}, observed output {observed}'


def test_atgc_gc_content():
    expected=0.5
    observed=gc_content('ATGC')
    assert observed==expected, f'worked-expected output {expected}, observed output {observed}'

def test_empty_gc_content():
    expected=0
    observed=gc_content('')
    assert observed==expected, f'worked-expected output {expected}, observed output {observed}'

def test_atat_gc_content():
    expected=0
    observed=gc_content('ATAT')
    assert observed==expected, f'worked-expected output {expected}, observed output {observed}'

def test_lowercase_gc_content():
    expected=0.5
    observed=gc_content('atgc')
    assert observed==expected, f'worked-expected output {expected}, observed output {observed}'

def test_randomchar_gc_content():
    try:
        observed=gc_content('ATGXB')
    except ValueError:
        return
    assert False,'expected ValueError'

def test_N_gc_content():
    expected=0.3
    observed=gc_content('ATGNNNTAGC')
    assert observed==expected, f'worked-expected output {expected}, observed output {observed}'

 