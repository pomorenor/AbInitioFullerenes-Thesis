import sys

#def explore_output(file_path, registerfile, x_variable, word = "TOTAL POTENTIAL ENERGY    =           "):
def explore_output(file_path, registerfile, x_variable, word = "LOWEST LYING STATES CONFIGURATION COEFFICIENTS"):
    TE = 0.0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines)):
            if lines[i].find(word) != -1:
              TE = lines[i+2].replace(" ","")
    with open(registerfile, 'a') as record:
        record.write(str(x_variable) + "\t" + str(TE)) 
    
    
    

path = sys.argv[1]
register = sys.argv[2]
xvariable = sys.argv[3]

explore_output(path, register, xvariable)