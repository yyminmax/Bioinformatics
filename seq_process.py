#!usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import numpy as np

base = ['A','T','C','G']
fp = open(sys.argv[1],'r')
fp1 = open(sys.argv[2],'r')
fp3 = open('summmary.txt','w')

content = fp.readlines()
msg_bases = fp1.readlines()

fp.close()

fp2 = open(sys.argv[1],'w')

#print content


Main = 'AA'
BC = []

#count_sample = np.zeros(len(content) - 1, dtype = np.int32)
count_sample = [0]*(len(content) - 1)
#for num_sample < 64
#print count_sample

for i in base:
	for j in base:
		for k in base:
			BC.append(Main + i + j + k)
fp2.write(content[0])
#del content[0]
sample = []

for i in range(1,len(content)):
	row = content[i].split('\t')
	del row[1]
	sample.append(row[0])
	row.insert(1,BC[i-1])
	fp2.write('\t'.join(row))
	#count_row = 0
	for j in range(len(msg_bases)):
		if(j % 2 != 0):
			continue
		if(msg_bases[j].strip('>').strip('\n') == row[0]):
			count_sample[i-1] += 1
			msg_bases[j] = msg_bases[j].strip('\n')
			msg_bases[j] += ('_' + str(count_sample[i-1]) + '\n')
			msg_bases[j+1] = BC[i-1] + msg_bases[j+1]	
fp2.close()
fp4 = open('clean.fna','w')

#print count_sample

for line in msg_bases:
	fp4.write(line)
for i in range(len(count_sample)):
	fp3.write(str(sample[i]) + '\t' + str(count_sample[i]) + '\n')

fp3.close()
fp4.close()

os.system("split_libraries.py -f clean.fna -l 150 -m map.txt -o split_out -b 5 -a 0 -M 1 -e 0 -H 8")
os.system("identify_chimeric_seqs.py -m usearch61 -i split_out/seqs.fna -o chimera_check --suppress_usearch61_ref --threads=24")
os.system("filter_fasta.py -f split_out/seqs.fna -o seqs.fna -s chimera_check/chimeras.txt -n")
