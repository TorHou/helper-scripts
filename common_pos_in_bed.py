import argparse
import sys

# User Variables
parser = argparse.ArgumentParser(description="Detect blocks of overlapping reads using a gaussian distribution approach.")
parser.add_argument("file1", help="bed file 1")
parser.add_argument("file2", help="bed file 2")
parser.add_argument("file3", help="bed file 3")
args = parser.parse_args()

pos = {}

with open (args.file1) as f:
    for line in f:
        sline=line.split("\t")
        beg = int(sline[1])
        end = int(sline[2])
        for i in range(beg,end+1):
            key = sline[0]+"_"+sline[5].rstrip()+"_"+str(i)
            pos[key] = "1"
            
with open (args.file2) as f:
    for line in f:
        sline=line.split("\t")
        beg = int(sline[1])
        end = int(sline[2])
        for i in range(beg,end+1):
            key = sline[0]+"_"+sline[5].rstrip()+"_"+str(i)
            if pos[key]:
                pos[key] += "2"
            else:
                pos[key] = "2"

with open (args.file3) as f:
    for line in f:
        sline=line.split("\t")
        beg = int(sline[1])
        end = int(sline[2])
        for i in range(beg,end+1):
            key = sline[0]+"_"+sline[5].rstrip()+"_"+str(i)
            if pos[key]:
                pos[key] += "3"
            else:
                pos[key] = "3"

allpos = 0.0
in1 = 0.0
in2 = 0.0
in3 = 0.0
in12 = 0.0
in13 = 0.0
in23 = 0.0
in123 = 0.0
for key,value in pos.iteritems():
    allpos += 1
    if value == "1":
        in1 += 1
    if value == "2":
        in1 += 2
    if value == "3":
        in1 += 3
    elif value == "12":
        in1 += 1
        in2 += 1
        in12 += 1
    elif value == "13":
        in1 += 1
        in3 += 1
        in13 += 1
    elif value == "23":
        in2 += 1
        in3 += 1
        in23 += 1
    elif value == "123":
        in1 += 1
        in2 += 1
        in3 += 1
        in12 += 1
        in13 += 1
        in23 += 1
        in123 += 1

print "in1: " + str(in1/allpos)
print "in2: " + str(in2/allpos)
print "in3: " + str(in3/allpos)
print "in12: " + str(in12/allpos)
print "in13: " + str(in13/allpos)
print "in23: " + str(in23/allpos)
print "in123: " + str(in123/allpos)
