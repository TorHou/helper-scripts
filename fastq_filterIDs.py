import argparse
from Bio import SeqIO

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("fastqfile")
arg_parser.add_argument("idfile")
arg_parser.add_argument("--deplete", default=False, action="store_true")

args=arg_parser.parse_args()

ids=set()

with open(args.idfile) as f:
    for line in f:
        rid = line.rstrip().split()[0]
        ids.add(rid)

fastq_sequences = SeqIO.parse(open(args.fastqfile),'fastq')


for fastq in fastq_sequences:
    if deplete:
        if fastq.id not in ids: print(fastq.format("fastq").rstrip())
    else: 
        if fastq.id in ids: print(fastq.format("fastq").rstrip())
