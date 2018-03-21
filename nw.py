import random
from Bio.Seq import Seq
from Bio import pairwise2
import sys

seq1 = Seq("GCGCCTA")
seq2 = Seq("GCTA")

sigma = "A C G T".split()

counter = 0 


def gap_function(x, y): 
    return -1

while True:
    seq1 = [random.choice(sigma) for _ in range(7)]
    seq1 = ''.join(seq1)
    seq2 = [random.choice(sigma) for _ in range(4)]
    seq2 = ''.join(seq2)
    
    alignments = pairwise2.align.globalms(seq1, seq2, 1, 0, -1 , -1)

    #print "Nr. of alignments: " + str(len(alignments))
    
    if len(alignments) == 3 and int(alignments[0][2])> 0:
        print alignments[0]
        print alignments[0][2]
        #if int(alignments[0][2])> 1: 
        for alignment in alignments:
            print(pairwise2.format_alignment(*alignment))
        print "Nr. of iterations needed: " + str(counter)
        sys.exit(0)
    else:
        counter += 1

