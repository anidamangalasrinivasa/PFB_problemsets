#!/usr/bin/env python3

#create a variable that stores dna sequence
pos_control='ATTGGGCCCC'
test='GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGccccTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACttttCG'

#do something about the case of the nucleotide characters
pos_control_upper=pos_control.upper()
test_upper=test.upper()

#count A's
pos_control_A_count=pos_control_upper.count('A')
test_A=test_upper.count('A')

#count T's
pos_control_T_count=pos_control_upper.count('T')
test_T=test_upper.count('T')

#count C's
pos_control_C_count=pos_control_upper.count('C')
test_C=test_upper.count('C')

#count G's
pos_control_G_count=pos_control_upper.count('G')
test_G=test_upper.count('G')

#print output
print(f'Positive control sequence is {pos_control} and its nucleotide counts are\n\t A:{pos_control_A_count}, T:{pos_control_T_count}, G:{pos_control_G_count} and C:{pos_control_C_count}')
print(f'Test sequence (in uppercase) is \n {test_upper} \nand its nucleotide counts are \n\t A:{test_A}, T:{test_T}, G:{test_G} and C:{test_C}')
