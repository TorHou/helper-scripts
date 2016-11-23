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
            if key in pos:
                pos[key] |= 0b100
            else:
                pos[key] = 0b100
            
with open (args.file2) as f:
    for line in f:
        sline=line.split("\t")
        beg = int(sline[1])
        end = int(sline[2])
        for i in range(beg,end+1):
            key = sline[0]+"_"+sline[5].rstrip()+"_"+str(i)
            if key in pos:
                pos[key] |= 0b010
            else:
                pos[key] = 0b010

with open (args.file3) as f:
    for line in f:
        sline=line.split("\t")
        beg = int(sline[1])
        end = int(sline[2])
        for i in range(beg,end+1):
            key = sline[0]+"_"+sline[5].rstrip()+"_"+str(i)
            if key in pos:
                pos[key] |= 0b001
            else:
                pos[key] = 0b001

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
    if value == 0b100:
        in1 += 1
    elif value == 0b010:
        in2 += 2
    elif value == 0b001:
        in3 += 3
    elif value == 0b110:
        in12 += 1
    elif value == 0b101:
        in13 += 1
    elif value == 0b011:
        in23 += 1
    elif value == 0b111:
        in123 += 1
    else :
        print key + value

print "in1: " + str(in1) + "\t" + str(in1/allpos)
print "in2: " +  str(in2) + "\t" + str(in2/allpos)
print "in3: " +  str(in3) + "\t" + str(in3/allpos)
print "in12: " + str(in12) + "\t" +  str(in12/allpos)
print "in13: " + str(in13) + "\t" +  str(in13/allpos)
print "in23: " + str(in23) + "\t" +  str(in23/allpos)
print "in123: " + str(in123) + "\t" +  str(in123/allpos)
