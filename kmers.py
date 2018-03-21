import argparse
from Bio import SeqIO
import operator

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("inputfile")
arg_parser.add_argument("from")

arg_parser.add_argument("to")

args=arg_parser.parse_args()
bkmer = args.bkmer
skmer = args.skmer
kmers={}

fasta_sequences = SeqIO.parse(open(args.inputfile),'fasta')

a=bkmer.find(skmer)
e=a+len(skmer)

for i in range(0,a+1):
    kmers[bkmer[i:e]] = 0

for i in range(len(bkmer),e-1,-1):
    #print bkmer[a:i]
    kmers[bkmer[a:i]] = 0


for fasta in fasta_sequences:
    seq = fasta.seq.upper()
    for skmer in kmers:
        k = len(skmer)
        lstart = len(seq)-k
        for i in range(0,lstart+1):
            if seq[i:i+k]==skmer:
                kmers[skmer] += 1
    

for kmer in kmers:
    print "\t".join([kmer, str(kmers[kmer])])


            


