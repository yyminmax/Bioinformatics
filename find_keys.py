from sys import argv
import os
from time import sleep


def Creat_dic(L, label):
    d = {}
    for a in L:
        row = a.split(':') 
        fir = row[1].find('<' + label + '>')
        end = row[1].find('</' + label + '>')
        name = row[1][fir+3:end]
        d[int(row[0])] = name
    return d

def Find_keys(L, key):
    mid = len(L)/2
    fir = 0
    end = len(L)
    while(True):
        print mid
        sleep(2)
        if(key > L[mid] and key < L[mid + 1]):
            return mid
        elif(key > L[mid + 1]):
            mid = (mid + 1 + end)/2
            fir = mid + 1
        elif(key < L[mid]):
            mid = (mid + fir)/2
            end = mid - 1

if(__name__ == "__main__"):
    fp = open(argv[1], 'r')

    commander = 'grep -n "^B.*<b>.*</b>" ' + argv[1]
    commander1 = 'grep -n "^A" ' + argv[1]

    f = os.popen(commander)
    f1 = os.popen(commander1)

    L = f.read().split('\n')
    L1 = f1.read().split('\n')
    del L[-1]
    del L1[-1]

    d = Creat_dic(L, 'b')
    d1 = Creat_dic(L1, 'a')

    print Find_keys(sorted(d.keys()), 10000)
    print Find_keys(sorted(d1.keys()), 10000)
