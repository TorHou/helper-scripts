import argparse
from Bio import SeqIO

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("fastqfile")
arg_parser.add_argument("idfile")

args=arg_parser.parse_args()

ids={}

with open(args.idfile) as f:
    for line in f:
        ids[line.rstrip()]=1

fastq_sequences = SeqIO.parse(open(args.fastqfile),'fastq')


for fastq in fastq_sequences:
    if fastq.id in ids:
        print fastq.format("fastq").rstrip()
