#!/usr/bin/env python

import sys

if(len(sys.argv) != 2):
    print "No input file given"
    exit(1)
f = open(sys.argv[1],"r")
values = {}
index = {}
for line in f:
    rownum = [float(val) for val in line.strip().split(",")]
    l=rownum[1:]
    mylist = [rownum[0],sum(rownum[1:])/len(l),max(rownum[1:])]
    mystring = ','.join(map(str, mylist))
    print mystring
