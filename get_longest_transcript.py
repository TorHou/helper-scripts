import argparse
import sys

# User Variables
parser = argparse.ArgumentParser(description="Find number of genomic positions in annotation files.")
parser.add_argument("file1", help="file of interest")
args = parser.parse_args()


genes = {}

with open (args.file1) as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        sline=line.split("\t")
        gene = sline[0]
        transcript = sline[1]
        length = int(sline[2].strip())
        if gene in genes:
            if genes[gene]["length"] < length:
                genes[gene]["length"] = length
                genes[gene]["transcript"] = transcript
        else: 
            genes[gene] = {}
            genes[gene]["length"] = length
            genes[gene]["transcript"] = transcript

for gene in genes:
    #print gene
    print "\t".join([gene,genes[gene]["transcript"],str(genes[gene]["length"])])
