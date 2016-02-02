#!/usr/bin/env python
from __future__ import division
import os
import sys
import time


def Compare(seq1, seq2):
    lengths = min(len(seq1), len(seq2))
    List = []
    for i in range(lengths):
        if(seq1[i] != seq2[i]):
            L = [i+1, seq2[i]]
            List.append(L)
    return List

def Init_Data(temp):
    d = {}
    stan = {'A':0, 'T':0, 'C':0, 'G':0}
    for i in range(len(temp)):
        stan[temp[i][1]] += 1
        d[temp[i][0]] = stan
        stan = {'A':0, 'T':0, 'C':0, 'G':0} 
        #print d
        #time.sleep(4)
    return d

def Update(d, temp):
    stan = {'A':0, 'T':0, 'C':0, 'G':0}
    for i in range(len(temp)):
        if(temp[i][0] in d.keys()):
            d[temp[i][0]][temp[i][1]] += 1
        else:
            stan[temp[i][1]] += 1
            d[temp[i][0]] = stan
            stan = {'A':0, 'T':0, 'C':0, 'G':0}
    return d

def Cal(d):
    count = 0
    for i in d.keys():
        count += d[i]
    return count

fp = open(sys.argv[1], 'r')
fp1 = open('example1.txt', 'r')
fp2 = open('example2.txt', 'r')

ex1 = fp1.readline().strip('\n')
ex2 = fp2.readline().strip('\n')

content = fp.readlines()
num_sample = int(sys.argv[2])

L1 = {}
L2 = {}
sample = {}

for i,line in enumerate(content):
    if(i % 2 == 0):
        sample_id = line.strip('\n').strip('>')
        temp1 = Compare(ex1, content[i+1].strip('\n'))
        temp2 = Compare(ex2, content[i+1].strip('\n'))
        #print temp1
        if(sample_id in L1.keys()):
            print 'Update the dic'
            L1[sample_id] = Update(L1[sample_id], temp1)
            L2[sample_id] = Update(L2[sample_id], temp2)
            sample[sample_id] += 1
        else:
            print 'Ceate a table'
            L1[sample_id] = Init_Data(temp1)
            L2[sample_id] = Init_Data(temp2)
            sample[sample_id] = 1

fp3 = open('summary1.txt', 'w')
fp4 = open('summary2.txt', 'w')
bases = ['A', 'T', 'C', 'G']

for sample_id in L1.keys():
    fp3.write('sample_id ' + sample_id + '\n')
    temp = ['location', 'mutation_num_total', 'A', 'T', 'C', 'G', 'percent']
    fp3.write('\t'.join(temp) + '\n')
    for n in L1[sample_id].keys():
        count = Cal(L1[sample_id][n])
        L = [str(n), str(count)]
        for b in bases:
            L.append(str(L1[sample_id][n][b]))
        percent = count/sample[sample_id]
        L.append(str(percent))
        fp3.write('\t'.join(L) + '\n')
for sample_id in L2.keys():
    fp4.write('sample_id ' + sample_id + '\n')
    temp = ['location', 'mutation_num_total', 'A', 'T', 'C', 'G', 'percent']
    fp4.write('\t'.join(temp) + '\n')
    for n in L2[sample_id].keys():
        count = Cal(L2[sample_id][n])
        L = [str(n), str(count)]
        for b in bases:
            L.append(str(L2[sample_id][n][b]))
        percent = count/sample[sample_id]
        L.append(str(percent))
        fp4.write('\t'.join(L) + '\n')
fp4.close()
