#!/usr/local/bin/python


"""
Compare the list of orthologous from one species in different lists.
Ex. genes of sp1 orthologous to sp2 and sp3.
Used (in my case) to get a list of orthologous among the different species (from pair othologou analyses in OMA).

Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

Usage = Shared_Ortho.py -1 <ortho_sp2> -2 <ortho_sp3> -o <output>

Where: 
-1 = list of orthologous genes between the species of interest and sp2
-2 = list of orthologous genes between the species of interest and sp3
-o = name of the output file. List of genes from the species of interest orthologous to the other species

Options: -h for usage help
"""

import sys, getopt

# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"h1:2:o:")
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = Shared_Ortho.py -1 <ortho_sp2> -2 <ortho_sp3> -o <output>'
    print 'For help use Shared_Ortho.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 3 and opt == '-h':
        print '\n', 'Compare the list of orthologous from one species in different lists. Ex.: genes of sp1 orthologous to sp2 and sp3.', '\n'
        print 'Usage = Shared_Ortho.py -1 <ortho_sp2> -2 <ortho_sp3> -o <output>'
        print 'Where: -1 = list of orthologous genes between the species of interest and sp2'
        print '-2 = list of orthologous genes between the species of interest and sp3'
        print '-o = name of the output file. List of genes from the species of interest orthologous to the other species'
        sys.exit()
    elif len(arg) > 3:
        if opt in ("-1"):
            list1 = open(arg)
        if opt in ("-2"):
            list2 = open(arg)
        if opt in ("-o", "--output"):
            output = open(arg,"w")
    elif len(arg) < 3:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"


# Creating useful stuff

gene_list1 = []
gene_list2 = []


# Open the list of genes and save them in another list

for gene in list1:
    gene_name = gene.split("\n")
    gene_name = str(gene_name[0])
    gene_list1.append(gene_name)
    
for gene in list2:
    gene_name = gene.split("\n")
    gene_name = str(gene_name[0])
    gene_list2.append(gene_name)
    

# Compare gene lists and save  the genes that appear in both

for id in gene_list1:
    if id in gene_list2:
        output.write(id)
        output.write("\n")        

output.close()
