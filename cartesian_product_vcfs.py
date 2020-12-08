from argparse import ArgumentParser
from Bio import SeqIO


parser = ArgumentParser()
parser.add_argument("inputfiles", help="VCF files", nargs="+")
#todo add vcf output format flag
args = parser.parse_args()

print(args.inputfiles)
