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
args = parser.parse_args()

refseq = ""

seqs = {}
addedEquals2=[("N", "A"), ("N", "G"),("N","T"),("N","C"),("C","Y"),("T","Y"),("R","A"),("R","G"),("S","G"),("S","C"),("W","A"),("W","T"),("K","G"),("K","T"),("M","A"),("M","C")]
addedEquals=[("N", "A"), ("N", "G"),("N","T"),("N","C")]



for record in SeqIO.parse(args.reffile, "fasta"):
    refidx = record.id
    seqs[record.id] = str(record.seq).upper()


for record in SeqIO.parse(args.infile, "fasta"):
    seqs[record.id] = str(record.seq).upper()

# Calculation of distances, if necessary
for i1 in seqs.keys() - set([refidx]):
    s1, s2 = [seqs[i1],seqs[refidx]]
    res = edlib.align(s1, s2,task='path',additionalEqualities=addedEquals)
    print(res)



