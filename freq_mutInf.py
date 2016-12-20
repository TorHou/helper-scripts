from __future__ import division
import argparse
import operator
import math
import numpy as np
from numpy import inf
import sys
from Bio import SeqIO
import itertools


length = 0.0

arg_parser = argparse.ArgumentParser(description="Calculate frequencies of nucleotides and mutual information of pairs of nucleotides of a FASTA file.")

arg_parser.add_argument("inputfile",help="FASTA input file")

args=arg_parser.parse_args()

threshold = 0
kmer_affinities={}
kmers_many={}
filetype = ""
regions = {}
counts = np.zeros((106,106))
count = np.zeros(106)
nts = {"A","C","G","T"}
pc = {}

combos = {''.join(i) for i in (itertools.product(nts,nts))}

for combo in combos:
    pc[combo] = np.zeros((106,106))
sc = {"A": np.zeros(106),"C": np.zeros(106), "G": np.zeros(106), "T": np.zeros(106)}


fasta_sequences = SeqIO.parse(open(args.inputfile),'fasta')
for fasta in fasta_sequences:
    length += 1.0
    seq = fasta.upper()
    for i in range(0,106):
        char = seq[i]
        sc[char][i] += 1.0
        for j in range(i,106):
            if i == j:
                continue
            char2=seq[j]
            pc[char+char2][i][j] += 1.0

for i in range(0,106):
    for char in sc:
        sc[char][i] = sc[char][i]/length
    for j in range(i,106):
        for chars in pc:
            pc[chars][i][j] = pc[chars][i][j]/length
M = np.zeros((106,106))
#for i in range(0,106):

#    for j in range(0,106):
spc = {}
for combo in combos: 
    a1 = sc[combo[0]]
    a2 = sc[combo[1]]
    a1.shape = (106,1)
    a2.shape = (106,1)
    spc[combo] = np.dot(a1, a2.transpose())
    ln = np.log2(np.divide(pc[combo],spc[combo]))
    ln[ln == -inf] = 0
    ln[ln == inf] = 0
    ls = pc[combo]*ln
    M = M + ls 

np.savetxt('mutInf.dat', M)
np.savetxt('freqs.dat', [sc["A"],sc["C"],sc["G"],sc["T"]])



#print sc["C"]
#print pc["CA"]
