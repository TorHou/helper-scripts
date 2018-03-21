import xml.etree.ElementTree as elTree
import argparse


arg_parser = argparse.ArgumentParser(description="This program parses some Galaxy xml files.")

arg_parser.add_argument("inputfile",help="xml file to parse")

args=arg_parser.parse_args()



tree = elTree.parse(args.inputfile)
root = tree.getroot()

for tool in root.iter('section'):
    print tool.get('name')
