import sys, re
import numpy as np
import pandas as pd
from ete3 import Tree
#print sys.argv
t = Tree("mtDNA_EntireTree.nw", format=1)
#print t.get_ascii(show_internal=True, attributes=["name", "snp"])
df = pd.read_csv('tree_query_out_12May.txt', sep="\s", header=None)
nodes = []
subtree = Tree()
for index, row in df.iloc[0:].iterrows():
    if pd.isnull(row[1]):
        node_name = 'NULL'
        print t.search_nodes(name = 'NULL')
    else:
        node_name = row[1]
    nodes = t.search_nodes(name = node_name)
    node = nodes[0]
    path = []
    while node.up:
        path.append(node)
        node = node.up
    current_node = subtree.get_tree_root()
    for n in reversed(path[:-1]):
        nnode = subtree.search_nodes(name = n.name)
        #print nnode
        if nnode:
            current_node = nnode[0]
        else:
            nn = current_node.add_child(name=n.name)
            nn.add_feature('snp', n.snp)
            current_node = nn
    #subtree.show()
    #break
subtree.write(format=1, features=["snp"], outfile="subtree_output_12May.nw")
#print subtree.get_ascii(attributes=["name", "snp"])
#print t.get_monophyletic(values=['K2b2', 'K2c'], target_attr="name")
#circular_style = TreeStyle()
#t.show(tree_style=circular_style)
