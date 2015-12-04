#!usr/bin/python
# -*- coding:utf-8 -*-

# this python file is used for calculating and 
# counting the OTU_number

import os 
import sys
import numpy as np

fp = open(sys.argv[1],'r')            #input file
fp1 = open('OTU_count.txt','w')       #output file
fp.readline()                 #skip the first line

sample = fp.readline().split('\t')
del sample[0]
del sample[len(sample)-1]
#delete the OTU_names and Taxa

#print len(sample)

Count_Matrix = np.zeros(len(sample)*7,dtype=np.int32).reshape(len(sample),7)
# Creat a Matrix for OTU_counting

for line in fp:
	row = line.split('\t')
	del row[0]
	if(row[len(row)-1] == 'No blast hit\n' or row[len(row)-1] == 'Unclassified\r\n'):
	# For no blast hit count
		for i in range(len(sample)):
			if(row[i] != '0'):
				Count_Matrix[i][6] = Count_Matrix[i][6] + 1
		continue
	otus = row[len(row)-1].split(';')
	num = 7        #init the number of taxa
	if(row[len(row)-1].find('__') != -1):
		for i in range(len(otus)):
			pick = otus[i].split('__')
			if(len(pick) < 2):
				print pick    #Check the taxa number in Greengenes,Unite 
			if(pick[1] == '' or pick[1] == '\n'):
				num = i
				break
	else:
		num = len(otus)     #Check the taxa number in RDP , Silva
	for i in range(len(sample)):
		if(row[i] != '0'):
			for j in range(num-1):
				Count_Matrix[i][j] = Count_Matrix[i][j] + 1

info = '\t'.join(['Sample','p','c','o','f','g','s','u']) + '\n'       #Creat the outputfile's label
fp1.write(info)
for i in range(len(sample)):
	L = []
	for j in range(7):
		L.append(str(Count_Matrix[i][j]))
	L.insert(0,sample[i])
	line = '\t'.join(L) + '\n'
	fp1.write(line)                                     #Write the output file


fp1.close()
fp.close()
