import sys, re
import numpy as np
import pandas as pd
import re
from ete3 import Tree, TreeStyle, TextFace, NodeStyle
#print sys.argv
t = Tree("/Users/weiwei/Downloads/outtree_B", format=1)
for n in t.traverse():
   if "unknown" not in n.name :
	#n.add_face(TextFace(n.name,fsize=20),  column=0)  #circle
	n.add_face(TextFace(n.name,fsize=10),  column=0)

df = pd.read_csv('tree_query_out.txt', sep="\s", header=None)
for index, row in df.iterrows():
    if pd.isnull(row[1]):
        node_name = 'NULL'
        print row[1]
    else:
        node_name = row[1]
    nodes = t.search_nodes(name = node_name)
    node = nodes[0]
    nstyle = NodeStyle()
    nstyle["fgcolor"] = "red"
    nstyle["size"] =8

    node.set_style(nstyle)
    node.add_face(TextFace(row[0],node.name,fsize=8 ), column=0)


ts = TreeStyle()
ts.show_leaf_name = False
ts.mode = "c"  #circle
ts.arc_start = -180 # 0 degrees = 3 o'clock
ts.arc_span = 180
t.ladderize()
t.render("mytree_T3394C.png", tree_style=ts)
t.show(tree_style=ts)
