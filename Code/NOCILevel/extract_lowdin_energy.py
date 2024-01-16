import sys

def explore_output(file_path, registerfile, x_variable, word = "TOTAL POTENTIAL ENERGY    =           "):
    TE = 0.0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(word) != -1:
                split_energy_line = line.split()
                TE = float(split_energy_line[len(split_energy_line)-1])

    with open(registerfile, 'a') as record:
        record.write(str(x_variable) + "\t" + str(TE) + "\n") 
        
    
    

path = sys.argv[1]
register = sys.argv[2]
xvariable = sys.argv[3]

explore_output(path, register, xvariable)