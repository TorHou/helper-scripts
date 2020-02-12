#!/usr/bin/env python3
import argparse
from Bio import SeqIO

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("fastaqfile")
arg_parser.add_argument("idfile")
arg_parser.add_argument("--format", help="[fasta*|fastq], *:default", default="fasta" )


args=arg_parser.parse_args()

ids={}

with open(args.idfile) as f:
    for line in f:
        ids[line.rstrip()]=1

fastaq_sequences = SeqIO.parse(open(args.fastaqfile),args.format)


for fastaq in fastaq_sequences:
    if fastaq.id in ids:
        print(fastaq.format(args.format).rstrip())
