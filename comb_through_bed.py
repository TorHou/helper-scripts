import argparse
import sys


parser = argparse.ArgumentParser(description="Check bed file.")
parser.add_argument("bedfile", help="bed file 3")
args = parser.parse_args()

genes = {}

with open(args.bedfile) as f:
    for line in f:
        sline = line.split()
        idx = sline[0]+"_"+sline[1]
        if not idx in genes:
            genes[idx] = sline[2]
        elif genes[idx] != sline[2]:
            print genes[idx] + line.strip()
        

