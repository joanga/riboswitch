# This script takes a file containing the the sequence IDs (sysargv 1) of an alignment from rfam. Then, it will read each line and identify which IDs refer to thermophilic organisms looking for the *therm expression in the genus and species. Then, it will takes the thermophilic ID lines and write them into the "thermos.txt" file. The other sequences are then pooled as mesophilic sequences and are stored in the "meso.txt" file. 


import re
import sys



input = open(sys.argv[1] , "r")
output1 = open("thermoID.txt", "w")
output2 = open("meso.txt", "w")

idfile = input.readlines()


for line in idfile:
	line = line.split()
	if not line[0].startswith("#"):
		if re.search(r"therm", line[3]) or re.search(r"Therm", line[3]):
			#line = ",".join(line)
			#line = line.replace("," , " ")
			output1.write(">" + str(line[0]) + "/"+ str(line[1]) + "-" + str(line[2]) + "\n")
		elif re.search(r"therm", line[4]) or re.search(r"Therm", line[4]):
			#line = ",".join(line)
			#line = line.replace("," , " ")
			output1.write(">" + str(line[0]) + "/"+ str(line[1]) + "-" + str(line[2]) + "\n")
		else:
			output2.write(">" + str(line[0]) + "/"+ str(line[1]) + "-" + str(line[2]) + "\n")

input.close()
output1.close()
output2.close()





