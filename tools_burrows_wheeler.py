#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools_karkkainen_sanders as tks
from array import array
import time

def dicho_find(l, val) :
  len_l = len(l)
  if val > l[-1] :
    return len_l
  elif val < l[0] :
    return 0
  start = 0
  end = len_l
  while start <= end:
    mid = int(start + ((end-start)/2))
    if(l[mid] == val) :
      break
    elif val > l[mid] :
      start = mid + 1
    else :
      end = mid - 1

  return mid

class BWT :
  def __init__(self, s) :
    self.s = s
    self.n = len(s)
    _,self.sa = tks.simple_kark_sort(s)
#    self.lcp = tks.LCP(s,self.sa)
    self.bwt = ''.join([s[self.sa[i]-1] for i in xrange(self.n)])
    self.n_alpha = {}
    self.occ = array('i',[0]*(self.n))
    self.dic_occ = {}
    self.small_dic_occ = {}
    for i,l in enumerate(self.bwt) :
      if l not in self.n_alpha :
        self.n_alpha[l] = 0
      self.n_alpha[l] += 1
      self.occ[i] = self.n_alpha[l]

    self.c = {}
    previous = 0
    list_letter = sorted(self.n_alpha.keys())
    for l in list_letter :
      self.c[l] = previous
      previous += self.n_alpha[l]


  def reverse_bwt(self) :
    i = 0
    j = self.n
    k = unicode('$','utf-8')
    t = array('u',u'_'*(self.n))
    while j > 0 :
      t[j-1] = k
      k = self.bwt[i]
      i = self.c[k] + self.occ[i] - 1
      j -= 1
    return t
    
  def prepare_search1(self) :
    dic_occ = {}
    for a in self.n_alpha.keys() :
      dic_occ[a] = [0]*(self.n+1)
      for i in xrange(self.n) :
        if self.bwt[i] == a :
          dic_occ[a][i+1] = dic_occ[a][i] + 1
        else :
          dic_occ[a][i+1] = dic_occ[a][i]
    self.dic_occ = {}
    for a,l in dic_occ.iteritems() :
      self.dic_occ[a] = l
      self.dic_occ[a].append(l[-1])
    
  def search1(self,pattern) :
    if self.dic_occ == {} :
      self.prepare_search1()
    i = len(pattern) - 1
    a = 1
    b = self.n
    while a <= b and i >= 0 :
      k = pattern[i]
      if k not in self.c :
        return 0
      a = self.c[k] + self.dic_occ[k][a-1] +1
      b = self.c[k] + self.dic_occ[k][b]
      i -= 1
    if b < a :
      return 0
    return b-a+1

  def prepare_search2(self) :
    self.small_dic_occ = dict((a,[]) for a in self.n_alpha.keys())
    for i,l in enumerate(self.bwt) :
      self.small_dic_occ[l].append(i)
    
  def get_occ(self, k, a) :
    l = self.small_dic_occ[k]
    res = dicho_find(l,a)
    return res

  def search2(self, pattern) :
    if self.small_dic_occ == {} :
      self.prepare_search2()
    i = len(pattern) - 1
    a = 1
    b = self.n
    while a <= b and i >= 0 :
      k = pattern[i]
      if k not in self.c :
        return 0
      a = self.c[k] + self.get_occ(k,a-1)+1
      b = self.c[k] + self.get_occ(k,b)
      i -= 1
    if b < a :
      return 0
    return b-a+1

  def print_sa(self) :
    res = [self.s[i] for i in self.sa[:self.n]]
    return ''.join(res)

  def print_rotation_aux(self, i) :
    res = [self.s[o+i-self.n] for o in xrange(self.n)]
    return ''.join(res)

  def print_rotation(self) :
    res = [self.print_rotation_aux(i) for i in xrange(self.n)]
    print '\n'.join(res) 

