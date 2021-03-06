# Orthology
Scripts to find and manipulate orthologous


# List_uniqOrtho.py

Check the list of ortologous pairs from OMA and separate the uniq orthologous transcripts ID.
Used (in my case) to get a list of uniq transcripts from each pair of species to get the
final orthologous among all tested species.

Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

**Usage**
List_uniqOrtho.py -i *pair file* -1 *sp1 outprefix* -2 *sp2 outprefix* 

**Where** 
-i = orthologous pair file result from **OMA** for any two species
-1 = prefix of the outuput list for sp1 in the OMA file
-2 = prefix of the outuput list for sp2 in the OMA file

**Options**
-h for usage help


# Shared_Ortho.py

Compare the list of orthologous from one species in different lists.
Ex. genes of sp1 orthologous to sp2 and sp3.
Used (in my case) to get a list of orthologous among the different species (from pair othologou analyses in OMA).

Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

**Usage**
Shared_Ortho.py -1 *ortho_sp2* -2 *ortho_sp3* -o *output*

**Where** 
-1 = list of orthologous genes between the species of interest and sp2
-2 = list of orthologous genes between the species of interest and sp3
-o = name of the output file. List of genes from the species of interest orthologous to the other species

**Options**
-h for usage help


# Select_Ortho.py

Check the list of ortologous pairs from OMA and separate the orthologous of interest based on a list of ID provided by the user.
Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

Developed (in my case) to get only the orthology data from the genes that appear in all species. 

**Usage**
Select_Ortho.py -i *pair file* -l *list_interest* -o *output*

**Where** 
pair file = orthologous pair file result from **OMA** for any two species
list_interest = list of the genes ID you want to recover from the pair file (one per line). Only get the sp1 ID.
output = output with the orthology info (like reported by **OMA**) of the genes from the interest list

**Options**
-h for usage help



# Select_Ortho2.py

Check the list of ortologous pairs from OMA and separate the orthologous of interest based on a list of ID provided by the user.
Like Selcte_Ortho.py but for other input format
Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

Developed (in my case) to get only the orthology data from the genes that appear in all species (file format after cleaning 1-1). 

**Usage**
Select_Ortho2.py -i *pair file* -l *list_interest* -o *output*

**Where** 
pair file = orthologous pair file result from **OMA** for any two species
list_interest = list of the genes ID you want to recover from the pair file (one per line). Only get the sp1 ID.
output = output with the orthology info (like reported by **OMA**) of the genes from the interest list

**Options** 
-h for usage help


# One_Multi.py

Select only one orthologous from a 1:multi orthologous data (reported by OMA pairwise analyses).

Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

**Usage**
One_Multi.py -i *1:multi* -o *output prefix*

**Where** 
-i = table as the output from pairwise orthology analyses in **OMA** but only with **1:multi** orthologous type
-o = prefix for the output files. 2 outputs will be generated: *1- prefix_OMA.txt*, table containing the orthologous pairs
determinied by OMA as one group; *2- prefix_nogroup.txt*, table containing the putative orthologous pairs to be chosen by the user.

**Options**
-h for usage help



# Multi_One.py

Select only one orthologous from a multi:1 orthologous data (reported by OMA pairwise analyses).

Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

**Usage**
Multi_One.py -i *multi:1* -o *output prefix*

**Where** 
-i = table as the output from pairwise orthology analyses in **OMA** but only with **multi:1** orthologous type
-o = prefix for the output files. 2 outputs will be generated: *1- prefix_OMA.txt*, table containing the orthologous pairs
determinied by OMA as one group; *2- prefix_nogroup.txt*, table containing the putative orthologous pairs to be chosen by the user.

**Options**
-h for usage help



# Multi_Multi.py

Select only one orthologous from a multi:multi orthologous data (reported by OMA pairwise analyses).

Ref.: Altenhoff A et al., The OMA orthology database in 2015: function predictions, better plant support, synteny view and other improvements, Nucleic Acids Research, 2015, 43 (D1): D240-D249 (doi:10.1093/nar/gku1158).

**Usage**
Multi_Multi.py -i *multi:multi* -o *output prefix*

**Where**
-i = table as the output from pairwise orthology analyses in **OMA** but only with **multi:multi** orthologous type
-o = prefix for the output files. 2 outputs will be generated: *1- prefix_OMA.txt*, table containing the orthologous pairs
determinied by OMA as one group; *2- prefix_nogroup.txt*, table containing the putative orthologous pairs to be chosen by the user.

**Options**
-h for usage help
