import sys
import re

def change_coordinates(file_path, atom_line, x, y, z):

    with open(file_path, mode='r') as file:
        lines = file.readlines()
        atom_coordinates = lines[atom_line - 1]
        atom_coordinates2 = re.split(r'(\s+)', atom_coordinates)
        atom_coordinates2[4] = x
        atom_coordinates2[6] = y
        atom_coordinates2[8] = z
#        print(atom_coordinates2)
        templine = ''.join(map(str,atom_coordinates2))

    lines[atom_line - 1] = templine

    with open(file_path, mode='w') as file:
        file.writelines(lines)


#        lines[atom_line - 1] = templine



path = "/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Calculations/water2.lowdin"
change_coordinates(path,4, 8.0, 7.0, 7.5)
