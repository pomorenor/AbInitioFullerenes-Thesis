import sys
import re

def change_coordinates(file_path, atom_line, electron_line, dx, dy, dz):

    with open(file_path, mode='r') as file:
        lines = file.readlines()
        atom_coordinates = lines[atom_line - 1]
        atom_coordinates2 = re.split(r'(\s+)', atom_coordinates)

        initial_x = float(atom_coordinates2[4])
        initial_y = float(atom_coordinates2[6])
        initial_z = float(atom_coordinates2[8])

        initial_x += dx
        initial_y += dy
        initial_z += dz

        atom_coordinates2[4] = str(initial_x)
        atom_coordinates2[6] = str(initial_y)
        atom_coordinates2[8] = str(initial_z)
#        print(atom_coordinates2)
        templine = ''.join(map(str,atom_coordinates2))

        ## Now we do the same for the electrons

        electron_coordinates = lines[electron_line - 1]
        electron_coordinates_2 = re.split(r'(\s+)', electron_coordinates)

        initial_x_el = float(electron_coordinates_2[4])
        initial_y_el = float(electron_coordinates_2[6])
        initial_z_el = float(electron_coordinates_2[8])

        initial_x_el += dx
        initial_y_el += dy
        initial_z_el += dz

        electron_coordinates_2[4] = str(initial_x_el)
        electron_coordinates_2[6] = str(initial_y_el)
        electron_coordinates_2[8] = str(initial_z_el)

        templine2 = ''.join(map(str,electron_coordinates_2))

    lines[atom_line - 1] = templine
    lines[electron_line - 1] = templine2

    with open(file_path, mode='w') as file:
        file.writelines(lines)


#        lines[atom_line - 1] = templine


path = sys.argv[1]
atom_line = int(sys.argv[2])
electron_line = int(sys.argv[3])
dx = float(sys.argv[4])
dy = float(sys.argv[5])
dz = float(sys.argv[6])



#path = "/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Calculations/water2.lowdin"
change_coordinates(path,atom_line,electron_line, dx, dy, dz)
