#!/usr/bin/env python3

import argparse
import random
import sys
from graph import Graph
from scc import SCC

parser = argparse.ArgumentParser(description='SCC client.')

parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin,
                    help='Input file with graph data (default stdin)')
parser.add_argument('-t', '--top', type=int, default=0,
                    help='Display only TOP components')
parser.add_argument('-s', '--sizes', action='store_true',
                    help='Display component sizes only')

args = parser.parse_args()
comp = SCC(Graph(args.infile))

num = args.top if args.top > 0 else None
items = comp.sizes(num) if args.sizes else comp.components(num)
for item in items:
    print(item)
