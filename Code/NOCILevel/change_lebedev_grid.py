import sys 

def change_grid(file_path):
	num_lines = 0
	with open(file_path, 'w') as file:
		lines = file.readlines()
		num_lines = len(lines)
	return num_lines 

path = sys.argv[1]
