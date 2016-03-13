#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sys import argv
import os

def print_help():
    print "Author: \nLastmodified: 2016-3-11"
    print "\t \t -i <infile>"
    print "\t \t -o <outpath> default: ./"
    print "\t \t -n <number of split file> dafault: 5"
    print "\t \t -h <help>"

if(__name__ == "__main__"):

    outpath = "./"
    num = 5
    if(len(argv) == 1):
        print_help()
        os._exit(0)

    if(argv[1] == "-h"):
        print_help()
        os._exit(0)

    infile = argv[argv.index('-i') + 1]
    if(argv.index('-o') != -1):
        outpath = argv[argv.index('-o') + 1]
    if(argv.index('-n') != -1):
        num = int(argv[argv.index('-n') + 1])

    if(str(outpath) != "." or str(outpath) != "./"):
        os.system("mkdir " + outpath)

    num_reads = int(os.popen("grep '>' " + infile + " | wc -l").read())
    print num_reads
    aver_reads = num_reads/num
    print aver_reads
    f = open(infile, 'r')
    #content = f.readlines()
    temp_str = ""

    for i in range(num):
        filename = outpath + '/' + str(i) + ".fa"
        fp = open(filename, 'w')
        count = 0
        if(i > 0):
            count = 1
        fp.write(temp_str)
        for line in f:
            if(i == num-1):
                fp.write(line)
                continue
            if('>' in line):
                count += 1
            print count
            if(count <= aver_reads):
                fp.write(line)
            else:
                fp.close()
                temp_str = line
                break

    fp.close()
