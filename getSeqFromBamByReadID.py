import argparse
from Bio import SeqIO
import pysam

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("bamfile")
arg_parser.add_argument("junctionfile")

args=arg_parser.parse_args()

ids=[]

with open(args.junctionfile) as f:
    for line in f:
        ids.append(line.split()[9])

print ids

samfile = pysam.AlignmentFile(args.bamfile, "rb")

iter = samfile.fetch("Plasmid")

for x in iter:
    if x.query_name in ids:
        print x.query_name
        print x.seq

iter = samfile.fetch("chr10")

for x in iter:
    if x.query_name in ids:
        print x.query_name
        print x.seq

iter = samfile.fetch("chr5")

for x in iter:
    if x.query_name in ids:
        print x.query_name
        print x.seq
