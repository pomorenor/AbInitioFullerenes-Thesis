import sys
import re

def compute_distance(x_1,y_1,z_1, x_2, y_2, z_2):
    return ((x_2 - x_1)**2 + (y_2 - y_1)**2+(z_2 - z_1)**2)**(1/2)


def obtain_atom_coordinates(file_path, atom_1_line, atom_2_line):
    distance = 0.0
    with open(file_path, mode='r') as file:
        lines = file.readlines()
        atom_1_coordinates = lines[atom_1_line - 1]
        atom_2_coordinates = lines[atom_2_line - 1]

        atom1 = re.split(r'(\s+)', atom_1_coordinates)
        atom2 = re.split(r'(\s+)', atom_2_coordinates)

        x_1 = float(atom1[4])
        y_1 = float(atom1[6])
        z_1 = float(atom1[8])

        x_2 = float(atom2[4])
        y_2 = float(atom2[6])
        z_2 = float(atom2[8])

        distance = compute_distance(x_1,y_1,z_1,x_2,y_2,z_2)

        return distance

path = sys.argv[1]
atom1_line = int(sys.argv[2])
atom2_line = int(sys.argv[3])

print(obtain_atom_coordinates(path, atom1_line, atom2_line))
