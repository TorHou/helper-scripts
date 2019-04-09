import argparse
from Bio import SeqIO
import sys

parser = argparse.ArgumentParser()

parser.add_argument("inputfile", help="Input in fasta")
args = parser.parse_args()

for read in SeqIO.parse(args.inputfile, "fasta"):
    with open(read.id + ".fasta", "w") as out:
        out.write(">" + read.id + "\n")
        out.write(str(read.seq))
