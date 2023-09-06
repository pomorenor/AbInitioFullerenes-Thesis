import sys
import re

def change_coordinates(file_path, atom_line, dx, dy, dz):

    with open(file_path, mode='r') as file:
        lines = file.readlines()
        atom_coordinates = lines[atom_line - 1]
        atom_coordinates2 = re.split(r'(\s+)', atom_coordinates)

        initial_x = float(atom_coordinates2[4])
        initial_y = float(atom_coordinates2[6])
        initial_z = float(atom_coordinates2[8])

        new_x = initial_x + dx
        new_y = initial_y + dx
        new_z = initial_z + dx

        atom_coordinates2[4] = str(new_x)
        atom_coordinates2[6] = str(new_y)
        atom_coordinates2[8] = str(new_z)
#        print(atom_coordinates2)
        templine = ''.join(map(str,atom_coordinates2))

    lines[atom_line - 1] = templine

    with open(file_path, mode='w') as file:
        file.writelines(lines)


#        lines[atom_line - 1] = templine



path = "/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Calculations/water2.lowdin"
change_coordinates(path,4, 8.0, 7.0, 7.5)
