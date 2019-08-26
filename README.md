# Phylogeny


##### Generate tree file ####
code: tree_gen.py
output: mtDNA_EntireTree.nw  

##### Query tree ####
code: tree_query.haploInput.py; tree_query.SNPinput.py  
input: mtDNA_EntireTree.nw & SNPs or nodes input files 
output: result_from_treequery.txt 

##### Generate subtree #####
code: subtree.py     
input: tree_query.py output 
output: subtree.nw

#### draw tree ####
code: tree_draw.py
input: subtree.py output subtree.nw
output: tree plot
