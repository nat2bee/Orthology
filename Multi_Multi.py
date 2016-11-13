#!/usr/local/bin/python


"""
Select only one orthologous from a multi:multi orthologous data (reported by OMA pairwise analyses).

Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

Usage = Multi_Multi.py -i <multi:multi> -o <output prefix>

Where: 
-i = table as the output from pairwise orthology analyses in OMA but only with multi:multi orthologous type
-o = prefix for the output files. 2 outputs will be generated: 1- prefix_OMA.txt, table containing the orthologous pairs
determinied by OMA as one group; 2- prefix_nogroup.txt, table containing the putative orthologous pairs to be chosen by the user.

Options: -h for usage help
"""

import sys, getopt

# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["input=","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = Multi_Multi.py -i <multi:1> -o <output prefix>'
    print 'For help use Multi_Multi.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if opt == '-h':
        print '\n', 'Select only one orthologous from a multi:multi orthologous data (reported by OMA pairwise analyses).', '\n'
        print 'Usage = Multi_Multi.py -i <multi:multi> -o <output prefix>'
        print 'Where: -i = table as the output from pairwise orthology analyses in OMA but only with multi:multi orthologous type'
        print '-o = prefix for the output files. 2 outputs will be generated: 1- prefix_OMA.txt, table containing the orthologous pairs determinied by OMA as one group; 2- prefix_nogroup.txt, table containing the putative orthologous pairs to be chosen by the user.'
        sys.exit()
    elif len(arg) >= 2:
        if opt in ("-i"):
            input = open(arg)
            rep_input = open(arg)
        if opt in ("-o", "--output"):
            name1 = arg + "_OMA.txt"
            output1 = open(name1,"w")
            name2 = arg + "_nogroup.txt"
            output2 = open(name2,"w")
    elif len(arg) < 2:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"


# Creating useful stuff

list_ID1 = []
list_ID2 = []


# Save the id of all the genes that are in a OMA group in a list and their line in the first output1

for line in input:
    elements = line.split("\t")
    if "NA\n" not in elements:
        id1 = str(elements[3:4])
        id2 = str(elements[4:5])
        list_ID1.append(id1)
        list_ID2.append(id2)
        output1.write(line)

# Save in output2 the orthologous groups not placed in any OMA group

for line in rep_input:
    elements = line.split("\t")
    if "NA\n" in elements:
        id1 = str(elements[3:4])
        id2 = str(elements[4:5])
        if id1 not in list_ID1 and id2 not in list_ID2:
            output2.write(line)

              

output1.close()
output2.close()
