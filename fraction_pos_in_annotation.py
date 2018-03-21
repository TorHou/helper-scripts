import argparse
import sys
import subprocess

# User Variables
parser = argparse.ArgumentParser(description="Find number of genomic positions in annotation files.")
parser.add_argument("file1", help="file of interest")
parser.add_argument("annotation", nargs="*", help="file1.bed label1 file2.bed label2 ....")
args = parser.parse_args()

if len(args.annotation)%2 != 0:
    print parser.print_help()
    sys.exit(0)



pos = {}
counter = {}
counter["total"] = 0

with open (args.file1) as f:
    for line in f:
        sline=line.split("\t")
        beg = int(sline[1])
        end = int(sline[2])
        counter["total"] += end - beg
        for i in range(beg,end+1):
            key = sline[0]+"_"+sline[5].rstrip()+"_"+str(i)
print "total: " + str(counter["total"])

for fname, label in zip(args.annotation[0::2], args.annotation[1::2]):
    sum = 0
    arguments = "bedtools intersect -wao -a "+args.file1 + " -b " + fname
    result=subprocess.check_output(arguments,shell=True)
    resultlines = result.split("\n")
    for line in resultlines:
        splitlines = line.split()
        if len(splitlines) < 13:
            continue
        #print len(splitlines)
        #print splitlines[len(splitlines)-1]
        sum = sum + int(line.split("\t")[12]) 
    print label + ": " + str(sum)
