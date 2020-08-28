from Bio import SeqIO
from argparse import ArgumentParser
from itertools import combinations
from collections import defaultdict
import edlib
import os
import sys
import pickle
import re


parser = ArgumentParser()
parser.add_argument("infile") 
parser.add_argument("reffile") 
parser.add_argument("vcfoutfolder") 
parser.add_argument("--calc_distances", action="store_true", default=False)
args = parser.parse_args()

refseq = ""

seqs = {}
addedEquals=[("N", "A"), ("N", "G"),("N","T"),("N","C"),("C","Y"),("T","Y"),("R","A"),("R","G"),("S","G"),("S","C"),("W","A"),("W","T"),("K","G"),("K","T"),("M","A"),("M","C")]
#addedEquals=[("N", "A"), ("N", "G"),("N","T"),("N","C")]


def parse_cigar(s1,s2,cigar,print_context=False):
    matches = re.findall(r'(\d+)([=XID]{1})', cigar)
    cp1 = 0
    cp2 = 0
    ps1 = []
    vars1 = []
    ps2 = []
    vars2 = []
    for m in matches:
        nrs, tp = m
        nr = int(nrs)
        if tp == 'X':
            ps1.append(list(range(cp1, cp1 + nr)))
            ps2.append(list(range(cp2, cp2 + nr)))
            vars1.append([s1[cp1:cp1+nr]])
            vars2.append([s2[cp2:cp2+nr]])
            cp1 += nr
            cp2 += nr
        elif tp == 'D':
            if cp1 >= len(s1):
                print("Problem: deletion not in sequence ... skipping")
                continue
            ps1.append([cp1])
            ps2.append(list(range(cp2,cp2+nr+1)))
            vars1.append([s1[cp1]])
            vars2.append([s2[cp2:cp2+nr+1]])
            cp2 += nr
        elif tp == 'I':
            if cp2 >= len(s2):
                print("Problem: insertion not in sequence ... skipping")
                continue
            ps1.append(list(range(cp1,cp1+nr+1)))
            ps2.append([cp2])
            vars1.append([s1[cp1:cp1+nr+1]])
            vars2.append([s2[cp2]])
            cp1 += nr
        elif tp == '=':
            cp1 += nr
            cp2 += nr
        else:
            print("Problem: Unknown cigar operation")
            sys.exit()
    return ps1,ps2,vars1,vars2

with open(args.reffile) as f:
    for line in f:
        if line.startswith(">"):
            refidx = line.rstrip().lstrip(">")
        else:
            refseq += line.rstrip().upper()

seqs[refidx] = refseq


for record in SeqIO.parse(args.infile, "fasta"):
    seqs[record.id] = str(record.seq).upper()

# Calculation of distances, if necessary
pfile = "pwalignments.pkl"
if args.calc_distances or not os.path.isfile(pfile):
    pwal= defaultdict(dict)
    for i1 in seqs.keys() - set([refidx]):
        s1, s2 = [seqs[i1],seqs[refidx]]
        res = edlib.align(s1, s2,task='path',additionalEqualities=addedEquals)
        pwal[i1] = res
    with open(pfile,"wb") as f:
        pickle.dump(pwal, f)
else:
    with open(pfile, "rb") as f:
        pwal=pickle.load(f)


# VCF header
header="""\
##fileformat=VCFv4.1
##contig=<ID=1,length=29903>
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT\
"""

# Generate VCF for each sequence in the input-fasta
for idx, result in pwal.items():
    fname = idx.replace("/","_") + ".vcf"
    with open(args.vcfoutfolder + "/" + fname, "w+") as outf:
        outf.write(header + "\t" + fname + "\n")
        print(idx)
        print(result)

        tings= parse_cigar(seqs[idx], seqs[refidx], result["cigar"])
        p1, p2, v1, v2 = tings
        for pos1, pos2, var1, var2 in zip(p1,p2,v1,v2):
            print("\t".join([refidx, str(pos2[0]+1), ".", var2[0], var1[0], ".", ".", ".", "GT", "1"]))
            outf.write("\t".join([refidx, str(pos2[0]+1), ".", var2[0], var1[0], ".", ".", ".", "GT", "1"]) + "\n")



##fileformat=VCFv4.1
##contig=<ID=1,length=29903>
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	hCoV-19/Wuhan/WIV04/2019|EPI_ISL_402124|2019-12-30|China	
#1	5	.	C	*,T	.	.	.	GT	1	1	1	1	1	1	1	1	
