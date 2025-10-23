## for BLASTP results:
    for m in BLOSUM62 BLOSUM80 PAM30 PAM70; do
    curl -O https://fasta.bioch.virginia.edu/mol_evol/data/blast_rand5-200_v_qfo_${m}.txt
    curl -O https://fasta.bioch.virginia.edu/mol_evol/data/blast_rand5-800_v_qfo_${m}.txt
    done