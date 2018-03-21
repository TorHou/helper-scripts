import argparse

def get_suffix_array(str): 
    return sorted(range(len(str)), key=lambda i: str[i:]) 



arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("sequence")

args=arg_parser.parse_args()

seq = args.sequence 
sa = get_suffix_array(seq)
print(sa)

for idx in sa:
    print(str(idx)  + ":\t" + seq[idx:])
