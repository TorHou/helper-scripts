import argparse
import sys


arg_parser = argparse.ArgumentParser(description="This program converts results from a cmsearch to a bed file with 6 columns.")

arg_parser.add_argument("inputfile",help="cmsearch result input file")
arg_parser.add_argument("--threshold",help="You can specify a threshold for the maximal E-value")

args=arg_parser.parse_args()


with open(args.inputfile) as f:
    for line in f:
        spline = line.split()
        if len(spline) >= 6 :
            if spline[5].startswith("chr"):
                printlineflag = True
                if args.threshold:
                    if float(spline[2]) > float(args.threshold):
                        printlineflag = False
                if printlineflag:
                    rs = "\t".join([spline[5],spline[6],spline[7],spline[0]+"_"+spline[2],"1.0",spline[8]])
                    print rs
                    
