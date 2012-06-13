#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tools_burrows_wheeler import BWT
import tools_karkkainen_sanders as tks
import time

s  = 'a'*10000
s += '$'
su = unicode(s,'utf-8','replace')

##
# precomputing data :
# - bwt.sa : suffix array of s
# - bwt.bwt : Burrows-Wheeler Transform
##

start_init = time.time()
bwt = BWT(su)
time_init = time.time() - start_init

print 'init : %s'%(time_init)

##
# construction of indexes
#  - bwt.prepare_search1() : huge index, quick access
#  - bwt.prepare_search2() : small index, log scale access
##

start_prepare_search1 = time.time()
bwt.prepare_search1()
time_prepare_search1 = time.time() - start_prepare_search1

start_prepare_search2 = time.time()
bwt.prepare_search2()
time_prepare_search2 = time.time() - start_prepare_search2

##
# search in s :
# - bwt.search1(pattern) : compute the frequency of pattern in s using huge index
# - bwt.search2(pattern) : compute the frequency of pattern in s using small index
##

pattern = 'a'*300

start_search1 = time.time()
count1 = bwt.search1(pattern)
print count1
time_search1 = time.time() - start_search1

start_search2 = time.time()
count2 = bwt.search2(pattern)
print count2
time_search2 = time.time() - start_search2

print 'method 1 : index construction %s, count %s'%(time_prepare_search1, time_search1)
print 'method 2 : index construction %s, count %s'%(time_prepare_search2, time_search2)
