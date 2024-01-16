import sys 

def change_grid(file_path, linenum, GridPoints):
	with open(file_path, 'r') as file:
		lines = file.readlines()
		gridline = lines[int(linenum)-1].rsplit('=')
		newline = gridline[0] + "=" + str(GridPoints) + "\n"
		lines[int(linenum)-1] = newline
		
		#with open(file_path, 'w') as file:
		#	file.writelines(lines)

		newname_endung = "_" + str(GridPoints) + "_" +"gridpoints" +'.lowdin'
		new_file_path =file_path.replace('.lowdin',newname_endung)

		with open(new_file_path, 'w') as new_file:
			new_file.writelines(lines)


path = sys.argv[1]
linenum = sys.argv[2]
gridpoints = sys.argv[3]
change_grid(path,linenum, gridpoints)