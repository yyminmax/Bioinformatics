# -*- coding: utf-8 -*-
"""
Author: yyminmax
Created on 
Last modified: 2016  5月 25
"""


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

fp = open(argv[1], 'r')
fp1 = open(argv[2], 'w')

L = ['domain', 'phylum', 'class', 'order', 'family', 'genus']
L1 = ['k__', 'p__', 'c__', 'o__', 'f__', 'g__']

s = fp.readline().split('\t')
s[0] = 'annotation'
del s[1]
fp1.write('\t'.join(s))

for line in fp:
    row = line.split('\t')
    print row
    d = {}
    taxon = row[0].split(';')
    for i in range(1, len(taxon), 2):
        d[taxon[i]] = taxon[i-1]
    if(row[1] not in L):
        row[1] = taxon[-2]
    if(row[1] not in L):
        row[1] = taxon[-3]
    if(row[1] not in L):
        row[1] = taxon[-4]
    spot = L.index(row[1])
    for i in range(spot+1):
        if(L[i] not in d.keys()):
            d[L[i]] = 'unclassified'
        if(i < spot):
            fp1.write(L1[i] + d[L[i]] + ';')
        else:
            fp1.write(L1[i] + d[L[i]] + '\t')
    lines = '\t'.join(row[2:6])
    fp1.write(lines)

fp.close()
fp1.close()
