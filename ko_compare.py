#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv 

def strip(s):
    return s.strip()

num = int(argv[1])

data = []

for i in range(num):
    data.append(map(strip, open(argv[i+2], 'r').readlines()))

for i in range(len(data)):
    data[i] = set(data[i])

print data
for i in range(num-1):
    for j in range(i+1, num):
        sum_k = data[i] | data[j]
        filename = argv[i+2].strip('.txt') + '-' + argv[j+2].strip('.txt') + '.txt'
        f = open(filename, 'w')
        for k in sorted(sum_k):
            if(k in data[i] and k in data[j]):
                f.write(k + '\t#color_both\n')
            elif(k in data[i] and k not in data[j]):
                f.write(k + '\t#color_1\n')
            elif(k not in data[i] and k in data[j]):
                f.write(k + '\t#color_2\n')
        f.close()
