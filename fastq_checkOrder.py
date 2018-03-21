import argparse
from Bio import SeqIO

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("fastqfile1")
arg_parser.add_argument("fastqfile2")

args=arg_parser.parse_args()


ids =[]

fastq_sequences1 = SeqIO.parse(open(args.fastqfile1),'fastq')


for fastq in fastq_sequences1:
    ids.append(fastq.id)

fastq_sequences2 = SeqIO.parse(open(args.fastqfile2),'fastq')
for idx, fastq in enumerate(fastq_sequences2):
    if ids[idx] != fastq.id:
        print str(idx) + "\t" + ids[idx] + "\t" + fastq.id
