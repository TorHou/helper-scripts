import argparse
from Bio import SeqIO

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("inputfile")
arg_parser.add_argument("contig")
arg_parser.add_argument("start", type=int)
arg_parser.add_argument("end", type=int)

args=arg_parser.parse_args()


with open(args.inputfile) as inf:
    for record in SeqIO.parse(inf,'fasta'):
        if args.contig == record.id:
            print(record.seq[args.start-1:args.end])


