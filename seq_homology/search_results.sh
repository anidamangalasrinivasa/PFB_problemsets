## for ssearch results:
    for m in BL50 BL62 VT10 VT20 VT40 VT80 VT160; do
    curl -O https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-200_v_qfo_${m}.txt
    curl -O https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-800_v_qfo_${m}.txt
    done

 