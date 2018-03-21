import argparse

parser = argparse.ArgumentParser()
parser.add_argument("rtscfile")
parser.add_argument("namefile")

args = parser.parse_args()

feats = set()
with open(args.namefile) as f:
    for line in f:
        feats.add(line.split()[0].split(">")[1])
print feats

investigate = False
with open(args.rtscfile) as f:
    for idx,line in enumerate(f):
        if investigate:
            ll = line.rstrip()
            a = [int(x) for x in ll.split()]
            if sum(a) > 10:
                print feature
                print "sum: ",str(sum(a))
            investigate = False
        if idx%3 == 0:
            #print line.rstrip()
            if line.rstrip() not in feats:
                feature = line.rstrip()
                investigate = True


