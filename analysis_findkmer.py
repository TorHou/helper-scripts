import argparse
from Bio import SeqIO
import operator
from sys import exit as ex

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("inputfile")
arg_parser.add_argument("kmer")

args=arg_parser.parse_args()
kmerio = args.kmer
kmers = []

p = kmerio.find("N")
if p != -1:
    kmers.append(kmerio[0:p]+"A"+kmerio[p+1:])
    kmers.append(kmerio[0:p]+"C"+kmerio[p+1:])
    kmers.append(kmerio[0:p]+"G"+kmerio[p+1:])
    kmers.append(kmerio[0:p]+"T"+kmerio[p+1:])
else:
    kmers.append(kmerio)

fasta_sequences = SeqIO.parse(open(args.inputfile),'fasta')


for fasta in fasta_sequences:
    sequ = fasta.seq.upper()
    for kmer in kmers:
        if kmer in sequ:
            print kmer + "\t" +str(fasta.id)


