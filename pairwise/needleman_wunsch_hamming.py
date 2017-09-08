#!/usr/bin/env python
# -*- coding: latin-1 -*-

import argparse
import numpy as np

gap_penalty = -1.0

def match_score(posA,posB):
  if posA == posB:
    return 1.0
  else:
    return -1.0

def align(seqA,seqB,print_dynamic_matrix = False):
  # Initiating variables
  n, m = len(seqA)+1, len(seqB)+1
  S = np.zeros((n,m))
  trace = np.zeros((n,m,2))
  # Set up dynamic programming matrices
  S[0,0] = 0.
  trace[0,0,:] = (0.,0.)
  for i in range(1,n):
    S[i,0] = gap_penalty * i
    trace[i,0,:] = (-1.,0.)
  for j in range(1,m):
    S[0,j] = gap_penalty * j
    trace[0,j,:] = (0.,-1.)
  # Set up dynamic programming matrices
  for i in range(1,n):
    for j in range(1,m):
      match = S[i-1][j-1] + match_score(seqA[i-1],seqB[j-1])
      delete = S[i-1][j] + gap_penalty
      insert = S[i][j-1] + gap_penalty
      S[i,j] = max(match, delete, insert)
      if match >= max(delete,insert):
        trace[i,j,:] = (-1,-1.)
      elif delete >= insert:
        trace[i,j,:] = (-1,0)
      else:
        trace[i,j,:] = (0,-1)
  if print_dynamic_matrix:
      print_dynamic(seqA,seqB,S)
  print("Best score: " + str(S[m-1,n-1]))
  return format_alignment(seqA,seqB,trace)

def format_alignment(seqA,seqB,trace):
  outA,outB = "",""
  i,j = len(seqA),len(seqB)
  while i>0 or j>0:
    di,dj = trace[i,j]
    i += int(di)
    j += int(dj)
    if di == 0:
      outA = "-" + outA
    else:
      outA = seqA[i] + outA
    if dj == 0:
      outB = "-" + outB
    else:
      outB = seqB[j] + outB
  return outA,outB

def print_alignment(seqA,seqB):
  print(seqA)
  print(seqB)

def print_dynamic(seqA,seqB,dpm):
  seqA,seqB = "-" + seqA, "-" + seqB
  m,n = len(seqA),len(seqB)
  print '{:^5}'.format(" "),
  for j in range(n):
    print '{:^5}'.format(seqB[j]),
  print
  for i in range(m):
    print '{:^5}'.format(seqA[i]),
    for j in range(n):
        print '{:5.1f}'.format(dpm[i,j]),
    print
  print

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('seqA', help='The First Sequence To Align')
  parser.add_argument('seqB', help='The Second Sequence To Align')
  parser.add_argument('--gap_penalty', type = float, default=-1., help='Gap Penalty')
  parser.add_argument('--print_dynamic_matrix', action='store_true', help='Print the dynamic programming matrix')
  args = parser.parse_args()
  global gap_penalty
  gap_penalty = args.gap_penalty
  seqA,seqB = align(args.seqA,args.seqB,args.print_dynamic_matrix)
  print_alignment(seqA,seqB)

if __name__ == "__main__":
   main()
