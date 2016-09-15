# riboswitch
#From rfam is its possible to download all the accession numbers and hits to the sequence from a family. However, rfam only host the seed alignment. 
If you want to build a full alignment, you will need to extract the sequences that are not part from of the seed from NCBI?

In my case, with this script I extract the names of the thermophilic organism form the 
accession numbers file and generate a  files to extract the sequences present in the seed alignment.
Note that there are thermophilic sequences that are not being evaluated becasue these sequences are not part of the seed alignment. 

How to use this scripts:

1. Use id extractor.py
  This script will require 
