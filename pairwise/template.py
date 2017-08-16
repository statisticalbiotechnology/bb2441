#!/usr/bin/env python
# -*- coding: latin-1 -*-

import argparse

def align(seqA,seqB):
  return (seqA,seqB)

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
