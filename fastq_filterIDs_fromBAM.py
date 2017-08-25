import argparse
from Bio import SeqIO
import pysam

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("fastqfile")
arg_parser.add_argument("bamfile")

args=arg_parser.parse_args()

ids=set()

bam = pysam.AlignmentFile(args.bamfile, "rb")
data = bam.fetch(multiple_iterators=True, until_eof=True)

for record in data:
   ids.add(record.query_name)

fastq_sequences = SeqIO.parse(open(args.fastqfile),'fastq')

for fastq in fastq_sequences:
    if fastq.id in ids:
        print fastq.format("fastq").rstrip()
