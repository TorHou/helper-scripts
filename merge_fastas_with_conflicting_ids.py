# This will take all the specified Fasta files in a specified directory
# and rename the id of the read to >${sample}_${old_id_up_to_first_whitespace}
# output can be either a file with a new header for each input
# or a combined FASTA for each sample
# or a combined FASTA for all files

from argparse import ArgumentParser
from yaml import load_all

'''
yaml-structure

---
- sample: hg003
  dir: .
  files: [3_1.fa, 3_2.fa]
- sample: hg004
  dir: .
  files: [4_1.fa, 4_2.fa]

'''

parser = ArgumentParser()
parser.add_argument("yaml_file", help="File containing all information for the FASTA files")
parser.add_argument("outfile_prefix", help="Specify the output file prefix.")
parser.add_argument("--mode", choices=["all", "sample", "each"], default="all", help="Select a mode, default is 'all'.")
args = parser.parse_args()

with open(args.yaml_file, 'r') as f:
    doc = list(load_all(f))[0]

if args.mode != "all":
    print("Mode " + str(args.mode) + " not implemented yet. Contact the author if you need this")
    
all_out = args.outfile_prefix + "_all.fasta"
aout = open(all_out, "w+")
for entry in doc:
    if "sample" not in entry or "dir" not in entry or "files" not in entry:
        print("Error parsing yaml")
    for input_file in entry["files"]:
        path = entry["dir"] + "/" + input_file
        with open(path, "r") as f:
            for line in f:
                if line.startswith(">"):
                    cid = line.split()[0][1:]
                    aout.write(">" + entry["sample"] + "_" + cid + "\n")
                else:
                    aout.write(line)

aout.close()
