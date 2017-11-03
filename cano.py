import re
a="""
neighbor-dump -t 0 -l 3 | grep  -A 12 '^4031 '
4031  0007810900dc0b93 MPD    true     00001 OFDM_600   OFDM_600   -21.572   -22       8PSK       19.727    21        102      330         11      false    
Last Unicast Reception Time: --------

Modulation list:
Modulation ModID ETTPHY  ETTEVAL ETXPHY  ETXEVAL LEval rec_total  rec_hb     rec_ucast  rec_cheard rec_sbr    rec_bcast  tx_succ_uc tx_fail_uc tx_retr_uc 
ROBO       0900  0003    0003    1       1       true  39         0          0          38         0          1          0          0          0          
BPSK       0901  0002    0002    1       1       true  19         19         0          0          0          0          0          0          0          
QPSK       0902  0001    0001    1       1       true  20         20         0          0          0          0          0          0          0          
8PSK       0903  0001    0001    1       1       true  19         19         0          0          0          0          0          0          0          
FSK_75     0a08  0002    0002    1       1       true  54         17         0          37         0          0          0          0          0          
OFDM_200   0a43  0001    0001    1       1       true  19         19         0          0          0          0          0          0          0          
OFDM_600   0a46  0001    0001    1       1       true  809        18         15         774        0          2          29         0          29         
LONG_RANGE 0a81  0015    0000    1       0       false 0          0          0          0          0          0          0          0          0          
#
"""
original_dict={}
match=re.search(r'ROBO\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(....)\s+(\d+)\s+(\d+)\s',a)
original_dict['ROBO'] =match.group(8)
match=re.search(r'BPSK\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(....)\s+(\d+)\s+(\d+)\s',a)
original_dict['BPSK'] =match.group(8)
match=re.search(r'QPSK\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(....)\s+(\d+)\s+(\d+)\s',a)
original_dict['QPSK'] =match.group(8)
match=re.search(r'8PSK\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(....)\s+(\d+)\s+(\d+)\s',a)
original_dict['8PSK'] =match.group(8)
match=re.search(r'FSK_75\s+(....)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(....)\s+(\d+)\s+(\d+)\s',a)
original_dict['FSK_75'] =match.group(8)
match=re.search(r'OFDM_200\s+(....)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(....)\s+(\d+)\s+(\d+)\s',a)
original_dict['OFDM_200'] =match.group(8)
match=re.search(r'OFDM_600\s+(.+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(....)\s+(\d+)\s+(\d+)\s',a)
original_dict['OFDM_600'] =match.group(8)
match=re.search(r'LONG_RANGE\s+(0a81)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.+)\s+(\d+)\s+(\d+)\s',a)
original_dict['LONG_RANGE'] =match.group(8)


print (original_dict)
