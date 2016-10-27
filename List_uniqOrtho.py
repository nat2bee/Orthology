#!/usr/local/bin/python


"""
Check the list of ortologous pairs from OMA and separate the uniq orthologous transcripts ID.
Used (in my case) to get a list of uniq transcripts from each pair of species to get the
final orthologous among all tested species.

Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

Usage = List_uniqOrtho.py -i <pair file> -1 <sp1 outprefix> -2 <sp2 outprefix> 

Where: 
-i = orthologous pair file result from OMA for any two species
-1 = prefix of the outuput list for sp1 in the OMA file
-2 = prefix of the outuput list for sp2 in the OMA file

Options: -h for usage help
"""

import sys, getopt

# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:1:2:",["input=","sp1=","sp2="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = List_uniqOrtho.py -i <pair file> -1 <sp1 outprefix> -2 <sp2 outprefix>'
    print 'For help use List_uniqOrtho.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 3 and opt == '-h':
        print '\n', 'Check the list of ortologous pairs from OMA and separate the uniq orthologous transcripts ID', '\n'
        print 'Usage = List_uniqOrtho.py -i <pair file> -1 <sp1 outprefix> -2 <sp2 outprefix>'
        print 'Where: -i = orthologous pair file result from OMA for any two species'
        print '-1 = prefix of the outuput list for sp1 in the OMA file'
        print '-2 = prefix of the outuput list for sp2 in the OMA file'
        sys.exit()
    elif len(arg) > 3:
        if opt in ("-i", "--input"):
            ortho = open(arg)
        if opt in ("-1", "--asp1"):
            prefix1 = arg + "_uniq.txt"
            out1 = open(prefix1, "w")
        if opt in ("-2", "--output"):
            prefix2 = arg + "_uniq.txt"
            out2 = open(prefix2, "w")
    elif len(arg) < 3:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"

# Creating useful stuff

sp1_list = []
sp2_list = []


# Function to clean id name

def clean_id(id):
    id = id.split(" ")
    id = str(id[0])
    id = id.split("'")
    id = str(id[1:2])
    return id


# Read the orthologous file and save the IDs from sp1 and sp2 only once (no repetitions) in the output

for line in ortho:
    elements = line.split("\t")  
    sp1_id = str(elements[2:3])
    sp1_id = clean_id(sp1_id)
    sp2_id = str(elements[3:4])
    sp2_id = clean_id(sp2_id)
    if sp1_id not in sp1_list:
        sp1_list.append(sp1_id)
        out1.write(sp1_id)
        out1.write("\n")
    if sp2_id not in sp2_list:
        sp2_list.append(sp2_id)
        out2.write(sp2_id)
        out2.write("\n")

    

out1.close()
out2.close()
