# coding:utf-8 

import re
from time import sleep

fp = open('gbbct115.seq', 'r')

pattern = re.compile(r'^VERSION')
pattern1 = re.compile(r'^DEFINITION')
pattern2 = re.compile(r'.*ORGANISM')
pattern3 = re.compile(r'ORIGIN')
pattern4 = re.compile(r'ACCESSION')

flag = False
flag1 = False

info = open('info.txt', 'w')
tax = open('tax.txt', 'w')
fasta = open('fasta.txt', 'w')

for line in fp:
    m = pattern.match(line)
    m1 = pattern1.match(line)
    m2 = pattern2.match(line)
    m3 = pattern3.match(line)
    m4 = pattern4.match(line)
    if m:
        print line
        s = line.split('  ')
        gi = s[-1].strip()[3:]
        asso = s[-2]
        fasta.write('>gi|' + gi + '|\n')
    if m1:
        print line
        title = line.strip()
        flag1 = True
    if m4:
        flag1 = False
    if(flag1):
        title += line.strip()
    if m2:
        print line
    if m3:
        print line
        info.write("\t".join([gi, asso, title]) + '\n')
        flag = True
    if(line[:2] == '//'):
        flag = False
    if(flag):
#        fasta.write('>gi|' + gi + '|\n')
        row = line.split(' ')
        fasta.write(''.join(row).upper())
        
info.close()
tax.close()
fasta.close()
fp.close()
