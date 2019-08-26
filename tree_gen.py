import sys, re
import numpy as np
import pandas as pd
from ete3 import Tree
#print sys.argv
df = pd.read_csv(sys.argv[1], sep=",", header=None)
t = Tree() # Creates an empty tree
node = t.add_child(name = 'mt-MRCA')
node.add_feature('snp', 'NULL')
node.add_feature('x', -1)
node.add_feature('y', -1)

for index, row in df.iterrows():
    for i, haplogroup in enumerate(row):
        if not pd.isnull(haplogroup):
            if not pd.isnull(df.iloc[index, i+1]):
                annotation = df.iloc[index, i+1].strip()
                snp = annotation.split('  ')
                #print index, i, haplogroup, snp
                #print t.get_ascii(show_internal=True, attributes=["name", "x", "y"])
                uppers = t.search_nodes(x=i-1)
                #print uppers
                node = uppers[-1].add_child(name = haplogroup)
                node.add_feature('snp', snp)
                node.add_feature('x', i)
                node.add_feature('y', index)
                break
            else:
                haplogroup = 'unknown'
                annotation = df.iloc[index, i].strip()
                snp = annotation.split('  ')
                #print index, i-1, haplogroup, snp
                uppers = t.search_nodes(x=i-2)
                #print uppers
                node = uppers[-1].add_child(name = haplogroup + str(index))
                node.add_feature('snp', snp)
                node.add_feature('x', i-1)
                node.add_feature('y', index)
                break

print t.get_ascii(show_internal=True, attributes=["name", "position"])
#t.show()
t.write(format=1, features=["snp"], outfile="mtDNA_EntireTree.nw")
