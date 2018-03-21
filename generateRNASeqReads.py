import argparse
import random 

parser = argparse.ArgumentParser()
parser.add_argument("referenceGenomeFile")
parser.add_argument("nrOfReads", type=int, default=1000)
parser.add_argument("outputFile")
args = parser.parse_args()

seq = ""
qual = ['A','B','C','D']

with open(args.referenceGenomeFile) as ref:
    for i, line in enumerate(ref):
        if i != 0:
            seq += line.rstrip().upper()

out = open(args.outputFile,"w+")
        
for i in range(args.nrOfReads):
    st1 = random.randint(0, len(seq)-101)
    st2 = random.randint(st1, min(len(seq),st1+5000))
    out.write("@"+str(i)+"_"+str(st1)+"\n")
    read = seq[st1:st1+50]+seq[st2:st2+50]+"\n"
    out.write(read)
    #out.write(seq[st1:st1+100]+"\n")
    out.write("+\n")
    out.write(''.join([random.choice(qual) for _ in range(len(read)-1)])+"\n")
    
#for r in range(0,args.nrOfReads):

