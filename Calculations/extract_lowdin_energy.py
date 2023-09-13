import sys

def explore_output(file_path, word = "TOTAL ENERGY ="):
    TE = 0.0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(word) != -1:
                split_energy_line = line.split()
                TE = float(split_energy_line[len(split_energy_line)-1])
    return TE

path = sys.argv[1]
#path = "/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Calculations/water.out"

print((explore_output(path)))
