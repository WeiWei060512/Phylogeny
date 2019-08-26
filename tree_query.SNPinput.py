import sys, re
import numpy as np
import pandas as pd
from ete3 import Tree
print sys.argv
t = Tree("mtDNA_EntireTree.nw", format=1)
df = pd.read_csv('SNP_list.tsv', sep="\t")
for index, row in df.iterrows():
    #target=str(row['SNPs']) 
    target = str(row['tnt']) + str(row['Location']) + str(row['qnt'])
    for node in t.traverse():
        if hasattr(node,"snp"):
            if target in node.snp:
                print target, node.name, node.snp

