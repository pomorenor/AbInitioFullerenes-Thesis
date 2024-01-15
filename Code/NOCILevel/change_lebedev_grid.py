import sys 

def change_grid(file_path, linenum, GridPoints):
	num_lines = 0
	with open(file_path, 'r') as file:
		lines = file.readlines()
		gridline = lines[linenum].rsplit('=')
		newline = gridline[0] + "=" + str(GridPoints)
		lines[linenum] = newline
		print(newline)
	return num_lines 

path = sys.argv[1]
change_grid(path,17,80)