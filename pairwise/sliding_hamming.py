#!/usr/bin/env python
# -*- coding: latin-1 -*-

import argparse

def align(seqA,seqB):
  max_score = -1
  max_pos = None
  for pos in range(-len(seqB)+1,len(seqA)):
    score = hamming(seqA,seqB,pos)
    if score > max_score:
      max_score = score
      max_pos = pos
  print("Best score: " + str(max_score))
  return format_alignment(seqA,seqB,max_pos)

def format_alignment(seqA,seqB,pos):
  outA = "-" * max(-pos,0) + \
         seqA + \
         "-" * max(len(seqB)-len(seqA)+pos,0)
  outB = "-" * max(pos,0) + \
         seqB + \
         "-" * max(len(seqA)-len(seqB)-pos,0)
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

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('seqA', help='The First Sequence To Align')
  parser.add_argument('seqB', help='The Second Sequence To Align')
  args = parser.parse_args()
  seqA,seqB = align(args.seqA,args.seqB)
  print_alignment(seqA,seqB)

if __name__ == "__main__":
   main()
