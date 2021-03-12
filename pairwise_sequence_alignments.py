from Bio import SeqIO
from argparse import ArgumentParser
from itertools import combinations
from collections import defaultdict
import edlib
import os
import sys
import pickle
import re


parser = ArgumentParser()
parser.add_argument("infile") 
parser.add_argument("reffile") 
parser.add_argument("--model", default="strict", help="Choose either [strict] or lenient")
args = parser.parse_args()

refseq = ""

seqs = {}
addedEquals2=[("N", "A"), ("N", "G"),("N","T"),("N","C"),("C","Y"),("T","Y"),("R","A"),("R","G"),("S","G"),("S","C"),("W","A"),("W","T"),("K","G"),("K","T"),("M","A"),("M","C")]
addedEquals=[("N", "A"), ("N", "G"),("N","T"),("N","C")]



for nr, record in enumerate(SeqIO.parse(args.reffile, "fasta")):
    if nr > 0:
        print("Warning: More than one sequence was found in " + args.reffile)
        print("Only the first entry will be used as reference.")
        break
    refidx = record.description
    seqs[record.description] = str(record.seq).upper()


for record in SeqIO.parse(args.infile, "fasta"):
    seqs[record.description] = str(record.seq).upper()

for i1 in seqs.keys() - set([refidx]):
    s1, s2 = [seqs[i1],seqs[refidx]]
    print(i1)
    if args.model == "strict":
        res = edlib.align(s1, s2,task='path',additionalEqualities=addedEquals)
    elif args.model == "lenient":
        res = edlib.align(s1, s2,task='path',additionalEqualities=addedEquals2)
    else:
        print("Model must be either strict or lenient.")
        sys.exit()
    print(res)
    #print(str(i1) + "\t" + str(res))



