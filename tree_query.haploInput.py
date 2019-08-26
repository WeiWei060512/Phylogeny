import sys, re
import numpy as np
import pandas as pd
from ete3 import Tree
#print sys.argv
t = Tree("mtDNA_EntireTree.nw", format=1)
df = pd.read_csv('haplogroup_list.tsv', header=None, sep="\t")
for index, row in df.iterrows():
    node = t&row[0];
    path = []
    while node.up:
        print row[0], node.snp;
        path.append(node)
        node = node.up
   # print (path);


