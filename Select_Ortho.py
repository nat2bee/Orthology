#!/usr/local/bin/python


"""
Check the list of ortologous pairs from OMA and separate the orthologous of interest based on a list of ID provided by the user.
Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

Developed (in my case) to get only the orthology data from the genes that appear in all species. 

Usage = Select_Ortho.py -i <pair file> -l <list_interest> -o <output>

Where: 
pair file = orthologous pair file result from OMA for any two species
list_interest = list of the genes ID you want to recover from the pair file (one per line). Only get the sp1 ID.
output = output with the orthology info (like reported by OMA) of the genes from the interest list

Options: -h for usage help
"""

import sys, getopt

# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:l:o:",["input=","list=","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = Select_Ortho.py -i <pair file> -l <list_interest> -o <output>'
    print 'For help use Up_Annotation.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 3 and opt == '-h':
        print '\n', 'Check the list of ortologous pairs from OMA and separate the orthologous of interest based on a list of ID provided by the user.', '\n'
        print 'Usage = Select_Ortho.py -i <pair file> -l <list_interest> -o <output>'
        print 'Where: pair file = orthologous pair file result from OMA for any two species'
        print 'list_interest = list of the genes ID you want to recover from the pair file (one per line).Only get the sp1 ID.'
        print 'output = output with the orthology info (like reported by OMA) of the genes from the interest list'
        sys.exit()
    elif len(arg) >= 3:
        if opt in ("-i", "--input"):
            ortho = open(arg)
        if opt in ("-l", "--list"):
            list = open(arg)
        if opt in ("-o", "--output"):
            output = open(arg,"w")
    else:
        assert False, "unhandled option"

# Create useful stuff

genes = []


# Open the list of IDs and save them in a list

for ids in list:
    gene = ids.split("\n")
    gene = str(gene[0])
    genes.append(gene)
    

# Function to clean id name

def clean_id(id):
    id = id.split(" ")
    id = str(id[0])
    id = id.split("'")
    id = str(id[1:2])
    return id

# Read the orthologous file and check the id of sp1, if in list print the line in the output

for line in ortho:
    elements = line.split("\t")  
    sp1_id = str(elements[2:3])
    sp1_id = clean_id(sp1_id)
    if sp1_id in genes:
        output.write(line)


output.close()
