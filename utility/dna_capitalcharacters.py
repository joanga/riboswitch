import re
import sys

dna_input = open(sys.argv[1], "r")
dna = dna_input.read().rstrip("\n")
dna_output = open("capital_dna.txt", "w")

dna_1 = dna.replace("a", "A")
dna_2 = dna_1.replace("g", "G")
dna_3 = dna_2.replace("c" , "C")
dna_4 = dna_3.replace("t" , "T")

dna_output.write(dna_4)

dna_input.close()
dna_output.close()