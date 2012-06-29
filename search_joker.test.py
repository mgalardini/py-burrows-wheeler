#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tools_burrows_wheeler import BWT
import tools_karkkainen_sanders as tks
import time

#s = 'mississippi$'
s  = 'a'*1500000
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
bwt.prepare_search1()
print 'init : %s'%(time_init)
#print 'BWT : %s'%(bwt.bwt)
#print 'SA : %s'%(bwt.sa)

#print bwt.get_previous(0,3)

#joker_pattern = ['i','??','iss']

start_search = time.time()
joker_pattern = ['a','????????','a']

previous_locate = None

n = len(joker_pattern)
for j in xrange(n) :
  i = n - j - 1
  pattern = joker_pattern[i]
  if pattern[0] == '?' :
    len_joker = len(pattern)
    len_next_pattern = len(joker_pattern[i-1])
    deep = len_joker + len_next_pattern
    next_locate = set()
    for i in previous_locate :
      previous = i - deep #bwt.get_previous(i, deep)
      if previous >= 0 :
        next_locate.add(previous)
    previous_locate = next_locate
#    previous_locate = set([bwt.get_previous(i, deep) for i in previous_locate]) 
  else :
    start_locate = time.time()
    locate = bwt.locate1(pattern)
    time_locate = time.time() - start_locate
    print 'locate::%s'%time_locate
    if previous_locate == None :
      previous_locate = locate
    else :
      start_inter = time.time()
      previous_locate = set(locate).intersection(previous_locate)
      time_inter = time.time() - start_inter
      print 'inter::%s'%time_inter
  if len(previous_locate) == 0 :
    print 'None, just Tesla'
    break
time_search = time.time() - start_search
print len(previous_locate)
#print previous_locate
print time_search
#print previous_locate
1/0
for pattern in joker_pattern[:-1] :
  if pattern[0] == '?' :
    len_joker = len(pattern)
    len_next_pattern = len()
    pass
  else :
    locate = bwt.locate1(pattern)
    if previous_locate == None :
      previous_locate = locate
    else :
      previous_locate = set(locate).intersection(set(previous_locate))




first_part = 'i'
last_part = 'i'
joker_pattern = '%s??%s'%(first_part, last_part)

first_locate = bwt.locate1(first_part)
last_locate = bwt.locate1(last_part)

print first_locate

print last_locate
last_locate_previous = [bwt.get_previous(i,3) for i in last_locate]
print last_locate_previous

set_last = set(last_locate)
set_previous = set(last_locate_previous)

print set_last.intersection(set_previous)





1/0

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
# - bwt.locate1(pattern) : locate pattern in s using huge index
# - bwt.locate2(pattern) : locate pattern in s using small index
##

#pattern = 'a'*300
pattern = 'pi'

start_search1 = time.time()
locate1 = bwt.locate1(pattern)
time_search1 = time.time() - start_search1
print 'method 1 : pattern "%s" in "%s" at the offsets %s'%(pattern, s, locate1)

start_search2 = time.time()
locate2 = bwt.locate2(pattern)
time_search2 = time.time() - start_search2
print 'method 2 : pattern "%s" in "%s" at the offsets %s'%(pattern, s, locate2)

print 'time method 1 : index construction %s, locate %s'%(time_prepare_search1, time_search1)
print 'time method 2 : index construction %s, locate %s'%(time_prepare_search2, time_search2)

pattern = '?i'
res = bwt.locate_joker_test(pattern)



