import sys
import re 
import numpy as np

def explore_output(file_path, numrows, word=" Diagonalizing non orthogonal CI Hamiltonian Matrix..."):
    selected_rows = []
    energies_found = False 

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if word in line:
                energies_found = True
                continue 

            if energies_found and len(selected_rows) < int(numrows) + 6:
                selected_rows.append(line)
        

    #We convert to a numpy array so we can erase the first six columns

    slrow = np.array(selected_rows)
    removed_not_importan_info_rows = slrow[6:]

    clean_rows = ["ENERGY[E_H]"]

    for line in removed_not_importan_info_rows:
    	match = re.search(r'\d+\.\d+', line)
    	if match:
    		energy = match.group()
    		clean_rows.append(energy)

    # Now we write the energies 
    with open("NOCI_Energies.txt", "w") as output:
        for row in clean_rows:
            output.write(row + "\n") 

path = sys.argv[1]
numrows = sys.argv[2]
# path = "/Code/NOCILevel/He3-C60-1S1P1D-170-gridpoints-duplet.out"

explore_output(path, numrows)
