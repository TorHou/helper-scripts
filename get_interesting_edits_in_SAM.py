import argparse
from Bio import SeqIO
import pysam

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("samfile")
args=arg_parser.parse_args()

ids=[]

samfile = pysam.AlignmentFile(args.samfile, "rb")

for read in samfile.fetch():
    mdtag = read.get_tag("MD")
    #if not mdtag[1].isdigit():
    if mdtag[0] == "0":
        print mdtag
        print read

samfile.close()
