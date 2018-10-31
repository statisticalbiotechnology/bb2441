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

def match_score_pam(posA, posB):
  return PAM250[posA][posB]

def align(seqA, seqB, print_dynamic_matrix = False, score = match_score):
  # Initiating variables
  m, n = len(seqA)+1, len(seqB)+1
  S = np.zeros((m,n))
  trace = np.zeros((m,n,2))
  # Set up dynamic programming matrices
  S[0,0] = 0.
  trace[0,0,:] = (0.,0.)
  for i in range(1,m):
    S[i,0] = 0.
    trace[i,0,:] = (0.,0.)
  for j in range(1,n):
    S[0,j] = 0.
    trace[0,j,:] = (0.,0.)
  # Set up dynamic programming matrices
  for i in range(1,m):
    for j in range(1,n):
      match = S[i-1][j-1] + score(seqA[i-1],seqB[j-1])
      delete = S[i-1][j] + gap_penalty
      insert = S[i][j-1] + gap_penalty
      S[i,j] = max(match, delete, insert, 0.)
      if match >= max(delete,insert,0.):
        trace[i,j,:] = (-1,-1.)
      elif delete >= max(insert,0.):
        trace[i,j,:] = (-1.,0.)
      elif insert >= 0.:
        trace[i,j,:] = (0.,-1.)
      else:
        trace[i,j,:] = (0.,0.)
  if print_dynamic_matrix:
      print_dynamic(seqA,seqB,S)
  print("Best score: " + str(np.max(S)))
  return format_alignment(seqA,seqB,S,trace)

def format_alignment(seqA,seqB,score,trace):
  outA,outB = "",""
  i,j = np.unravel_index(score.argmax(),score.shape)
  while score[i,j]>0.:
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

def hamming(seqA,seqB,pos):
  seqA = seqA[max(pos,0):min(len(seqB)+pos,len(seqA))]
  seqB = seqB[max(-pos,0):max(len(seqA)-pos,len(seqB))]
  # print seqA,seqB,pos, max(-pos,0), max(len(seqA)-pos,len(seqA))
  matches = sum(el_a == el_b for el_a, el_b in zip(seqA, seqB))
  return matches

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

PAM250 = {
'A': {'A': 2,  'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N':  0, 'P':  1, 'Q':  0, 'R': -2, 'S':  1, 'T':  1, 'V':  0, 'W': -6, 'Y': -3},
'C': {'A': -2, 'C': 12, 'D': -5, 'E':-5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S':  0, 'T': -2, 'V': -2, 'W': -8, 'Y':  0},
'D': {'A': 0,  'C': -5, 'D':  4, 'E': 3, 'F': -6, 'G':  1, 'H':  1, 'I': -2, 'K':  0, 'L': -4, 'M': -3, 'N':  2, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
'E': {'A': 0,  'C': -5, 'D':  3, 'E': 4, 'F': -5, 'G':  0, 'H':  1, 'I': -2, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
'F': {'A': -3, 'C': -4, 'D': -6, 'E':-5, 'F':  9, 'G': -5, 'H': -2, 'I':  1, 'K': -5, 'L':  2, 'M':  0, 'N': -3, 'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W':  0, 'Y':  7},
'G': {'A': 1,  'C': -3, 'D':  1, 'E': 0, 'F': -5, 'G':  5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N':  0, 'P':  0, 'Q': -1, 'R': -3, 'S':  1, 'T':  0, 'V': -1, 'W': -7, 'Y': -5},
'H': {'A': -1, 'C': -3, 'D':  1, 'E': 1, 'F': -2, 'G': -2, 'H':  6, 'I': -2, 'K':  0, 'L': -2, 'M': -2, 'N':  2, 'P':  0, 'Q':  3, 'R':  2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y':  0},
'I': {'A': -1, 'C': -2, 'D': -2, 'E':-2, 'F':  1, 'G': -3, 'H': -2, 'I':  5, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -5, 'Y': -1},
'K': {'A': -1, 'C': -5, 'D':  0, 'E': 0, 'F': -5, 'G': -2, 'H':  0, 'I': -2, 'K':  5, 'L': -3, 'M':  0, 'N':  1, 'P': -1, 'Q':  1, 'R':  3, 'S':  0, 'T':  0, 'V': -2, 'W': -3, 'Y': -4},
'L': {'A': -2, 'C': -6, 'D': -4, 'E':-3, 'F':  2, 'G': -4, 'H': -2, 'I':  2, 'K': -3, 'L':  6, 'M':  4, 'N': -3, 'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V':  2, 'W': -2, 'Y': -1},
'M': {'A': -1, 'C': -5, 'D': -3, 'E':-2, 'F':  0, 'G': -3, 'H': -2, 'I':  2, 'K':  0, 'L':  4, 'M':  6, 'N': -2, 'P': -2, 'Q': -1, 'R':  0, 'S': -2, 'T': -1, 'V':  2, 'W': -4, 'Y': -2},
'N': {'A': 0,  'C': -4, 'D':  2, 'E': 1, 'F': -3, 'G':  0, 'H':  2, 'I': -2, 'K':  1, 'L': -3, 'M': -2, 'N':  2, 'P':  0, 'Q':  1, 'R':  0, 'S':  1, 'T':  0, 'V': -2, 'W': -4, 'Y': -2},
'P': {'A': 1,  'C': -3, 'D': -1, 'E':-1, 'F': -5, 'G':  0, 'H':  0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N':  0, 'P':  6, 'Q':  0, 'R':  0, 'S':  1, 'T':  0, 'V': -1, 'W': -6, 'Y': -5},
'Q': {'A': 0,  'C': -5, 'D':  2, 'E': 2, 'F': -5, 'G': -1, 'H':  3, 'I': -2, 'K':  1, 'L': -2, 'M': -1, 'N':  1, 'P':  0, 'Q':  4, 'R':  1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
'R': {'A': -2, 'C': -4, 'D': -1, 'E':-1, 'F': -4, 'G': -3, 'H':  2, 'I': -2, 'K':  3, 'L': -3, 'M':  0, 'N':  0, 'P':  0, 'Q':  1, 'R':  6, 'S':  0, 'T': -1, 'V': -2, 'W':  2, 'Y': -4},
'S': {'A': 1,  'C':  0, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P':  1, 'Q': -1, 'R':  0, 'S':  2, 'T':  1, 'V': -1, 'W': -2, 'Y': -3},
'T': {'A': 1,  'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  0, 'H': -1, 'I':  0, 'K':  0, 'L': -2, 'M': -1, 'N':  0, 'P':  0, 'Q': -1, 'R': -1, 'S':  1, 'T':  3, 'V':  0, 'W': -5, 'Y': -3},
'V': {'A': 0,  'C': -2, 'D': -2, 'E':-2, 'F': -1, 'G': -1, 'H': -2, 'I':  4, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -6, 'Y': -2},
'W': {'A': -6, 'C': -8, 'D': -7, 'E':-7, 'F':  0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4, 'P': -6, 'Q': -5, 'R':  2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y':  0},
'Y': {'A': -3, 'C':  0, 'D': -4, 'E':-4, 'F':  7, 'G': -5, 'H':  0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2, 'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W':  0, 'Y': 10}}


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('seqA', help='The First Sequence To Align')
  parser.add_argument('seqB', help='The Second Sequence To Align')
  parser.add_argument('--gap_penalty', type = float, default=-1., help='Gap Penalty')
  parser.add_argument('--print_dynamic_matrix', action='store_true', help='Print the dynamic programming matrix')
  parser.add_argument('--pam', action='store_true', help='Score with PAM250 matrix rather than inversed hamming distance')
  args = parser.parse_args()
  global gap_penalty
  gap_penalty = args.gap_penalty
  if args.pam:
    seqA,seqB = align(args.seqA,args.seqB,args.print_dynamic_matrix,match_score_pam)
  else:
    seqA,seqB = align(args.seqA,args.seqB,args.print_dynamic_matrix,match_score)
  print_alignment(seqA,seqB)

if __name__ == "__main__":
   main()
