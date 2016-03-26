#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from time import sleep
import re

def find_info(url, start, end):
    spot_Name_1 = url.find(start)
    spot_Name_2 = url.find(end)
    name = url[spot_Name_1 + len(start) : spot_Name_2]
    return name

#start_url = 'file:///C:/Users/lenovo/Desktop/Functional%20Gene%20Pipeline%20_%20Repository_1.htm'
base = 'http://fungene.cme.msu.edu/'

fp = open('Functional Gene Pipeline _ Repository.htm', 'r')

fp1 = open('E://WorkSpace//Scapy//index_3.txt', 'w')
fp2 = open('E://WorkSpace//Scapy//nosz_blast_3.fa', 'w')
fp3 = open('E://WorkSpace//Scapy//no_hit_3.txt', 'w')

content = fp.readlines()

pattern = re.compile(r'.*?<a href="http://fungene.cme.msu.edu/gbnucdata.jsp?.*?')

for line in content:
    m = pattern.match(line)
    #print line
    if(m):
        line = line.strip()
        first = line.find('"')
        last = line.find('"', first+1)
        url = line[first+1:last].replace('amp;', '').strip()
        print url
        row = url.replace('&strand=1&format=Genbank', '').split('?')
        fasta_url = row[0] + '?format=Fasta&' + row[1]
        print fasta_url
        name = find_info(url, 'Accno=', '&seq_start')
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
        try:
            r = requests.get(url, headers=headers)
            r1 = requests.get(fasta_url, headers=headers)
        except Exception,e:
            print('ConnectionError')
            fp3.write(name + '\t' + url + '\n')
            continue
        soup = BeautifulSoup(r.content, 'html.parser')
        soup1 = BeautifulSoup(r1.content, 'html.parser')
        info = str(soup.find('pre'))
        info1 = str(soup1.find('pre')).strip('</pre>').strip('<pre>').strip().replace('&gt;', '>')
        fp2.write(info1 + '\n')
        #name = find_info(url, 'Accno=', '&seq_start')
        #print name
        string = find_info(info, 'ORGANISM', 'REFERENCE')
        s = string.split('\n')
        for i in range(len(s)):
            s[i] = s[i].strip()
        new_string = s[1] + s[2]
        fp1.write(name + '\t' + new_string + '\n')
        #string = re.findall(r'ORGANISM.*?REFERENCE' ,str(soup.find('pre')))
        #print string
        #sleep(2)

fp.close()
fp1.close()
fp2.close()
fp3.close()
