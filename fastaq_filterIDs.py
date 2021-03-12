#!/usr/bin/env python3
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument('--format', choices=["fasta", "fastq"], default="fasta")
subparser = parser.add_subparsers(dest='mode')

by_idfile = subparser.add_parser('idfile')
by_pattern = subparser.add_parser('pattern')

by_idfile.add_argument('idfile')
by_idfile.add_argument('fastaqfile')
by_pattern.add_argument('pattern')
by_pattern.add_argument('fastaqfile')


args=parser.parse_args()

if args.mode == 'idfile':
    ids=set()
    with open(args.idfile) as f:
        for line in f:
            ids.add(line.rstrip())

    fastaq_sequences = SeqIO.parse(open(args.fastaqfile),args.format)
    for fastaq in fastaq_sequences:
        if fastaq.id in ids:
            print(fastaq.format(args.format).rstrip())
elif args.mode == 'pattern':

    fastaq_sequences = SeqIO.parse(open(args.fastaqfile),args.format)
    for fastaq in fastaq_sequences:
        if args.pattern in fastaq.description:
            print(">" + fastaq.description)
            print(str(fastaq.seq).upper())
