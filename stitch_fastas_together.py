import argparse
from Bio import SeqIO
import sys

parser = argparse.ArgumentParser()

parser.add_argument("inputfile", help="Input specifying patches")
parser.add_argument("outname", help="Identifier for output")
parser.add_argument("outputfile", help="Output in Fasta Format")
args = parser.parse_args()

out = open(args.outputfile,"w+")

with open(args.inputfile) as f:
    out.write(">" + args.outname + "\n")
    for line in f:
        print("Processing " + line.rstrip())
        if len(line.split()) == 4:
            whole_ctg = False
            ffile, contig, start, end = line.rstrip().split()
        else:
            whole_ctg = True
            ffile, contig, t1 = line.rstrip().split()
        if not ffile.endswith("fasta") and not ffile.endswith("fa"):
            print("Sequence files are not in fasta format. Aborting!")
            sys.exit()
        for read in SeqIO.parse(ffile, "fasta"):
            if read.id == contig:
                if whole_ctg:
                    out.write(str(read.seq))
                else:
                    out.write(str(read.seq)[int(start)-1:int(end)-1])
            #with open(read.id + ".fasta", "w") as out:
            #    out.write(">" + read.id + "\n")
            #    out.write(str(read.seq))
out.close()
