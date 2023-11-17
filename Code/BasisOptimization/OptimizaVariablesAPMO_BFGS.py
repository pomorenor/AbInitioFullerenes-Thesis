#!/usr/bin/python3

import numpy as np
import re
import sys
import os
import subprocess
from scipy.optimize import minimize
import numpy as np

###### Function to compute the norm ################

R_C = [0.0,0.0,0.0]

def norm(r, R):

    squared_norm = 0.0

    for i in range (0,len(R)):
        squared_norm += (R[i] - r[i])**2

    return np.sqrt(squared_norm)

####### New function to constrain the coordinates #########

def constraints_atom_1(coords):

    Vec_r_1 = [coords[0], coords[1], coords[2]]
    Vec_r_2 = [coords[3], coords[4], coords[5]]
    Vec_r_3 = [coords[6], coords[7], coords[8]]

    r_12 = norm(Vec_r_1, Vec_r_2)
    r_13 = norm(Vec_r_1, Vec_r_3)

    return r_12 - r_13

def constraints_atom_2(coords):

    Vec_r_1 = [coords[0], coords[1], coords[2]]
    Vec_r_2 = [coords[3], coords[4], coords[5]]
    Vec_r_3 = [coords[6], coords[7], coords[8]]

    r_21 = norm(Vec_r_2, Vec_r_1)
    r_23 = norm(Vec_r_2, Vec_r_3)

    return r_21 - r_23


def constraints_atom_3(coords):

    Vec_r_1 = [coords[0], coords[1], coords[2]]
    Vec_r_2 = [coords[3], coords[4], coords[5]]
    Vec_r_3 = [coords[6], coords[7], coords[8]]

    r_31 = norm(Vec_r_3, Vec_r_1)
    r_32 = norm(Vec_r_3, Vec_r_2)

    return r_31 - r_32



constraints = (
    {'type':'eq', 'fun':constraints_atom_1},
    {'type':'eq', 'fun':constraints_atom_2},
    {'type':'eq', 'fun':constraints_atom_3}
)




######### function to write coordinates
def writeCoords(inputName,coords):
    variablesFile=open(inputName,"w+")
    line="Script "+scriptName+"\n"
    variablesFile.write(line)
    line="NumVariables "+str(numberOfVariables)+"\n"
    variablesFile.write(line)

    for i in range(0,numberOfVariables):
        line="X"+str(i+1)+" "+str(coords[i])+"\n"
        variablesFile.write(line)

    variablesFile.close()

    return

######### function to extract energy
def getEnergy(outName):
    energy=0
    with open(outName) as out:
        for line in out:
            fields=line.strip().split()
            if(method=="HF" and len(fields)>1):
                if (re.match("TOTAL",fields[0]) and re.match("ENERGY",fields[1]) and re.match("=",fields[2])): energy=fields[3]
            if(method=="MP2" and len(fields)>0):
                if (re.match("E\(MP2\)=",fields[0]) ): energy=fields[1]
            if(method=="CI" and len(fields)>3):
                if(re.match("STATE:",fields[0]) and fields[1]=="1"): energy=fields[4]
            if(method=="COR" and len(fields)>4):
                if(re.match("CORRELATION",fields[2])): energy=fields[5]

    return float(energy)

######### function to write variables, run calculation, get energy
def energy(coords):
#
    writeCoords(coordsFile,coords)

    command=str("./"+scriptName+" "+coordsFile)
    os.system(command)

    energy=getEnergy(outName)
    print("at ", coords, "energy is", energy, flush=True)
    return energy

######### function to write variables, run calculation, get energy
def gradient(coords):
#
    gradient=np.zeros(numberOfVariables)
    for a in range(0,numberOfVariables):
        dispx=coords.copy()
        #displaces coordinate number a
        #step forward
        dispx[a]=coords[a]+step[a]

        writeCoords(coordsFile,dispx)
        command=str("./"+scriptName+" "+coordsFile)
        os.system(command)
        energyp=getEnergy(outName)
        # print(dispx[a],energyp)

        #step backward
        dispx[a]=coords[a]-step[a]
        writeCoords(coordsFile,dispx)
        command=str("./"+scriptName+" "+coordsFile)
        os.system(command)
        energym=getEnergy(outName)
        # print(dispx[a],energym)

        #calculate gradient in coordinate a
        gradient[a]=(energyp-energym)/(2*step[a])

    print("at ", coords, "gradient is", gradient, flush=True)
    return gradient


########## read input file

scriptName=""
numberOfVariables=0
method="HF"
solver="BFGS"
#solver = "SLSQP"
limit=1e-6
maxIterations=1000

#las variables deben ir en orden!
with open(sys.argv[1]) as inp:
    for line in inp:
        fields=line.strip().split()
        if len(fields)!=0:
            if(re.match("script",fields[0],re.I)): scriptName=fields[1]
            if(re.match("numvariables",fields[0],re.I)): numberOfVariables=int(fields[1])
            if(re.match("method",fields[0],re.I)): method=fields[1]
            if(re.match("solver",fields[0],re.I)): solver=fields[1]
            if(re.match("limit",fields[0],re.I)): limit=float(fields[1])
            if(re.match("maxiter",fields[0],re.I)): maxIterations=int(fields[1])
    initialValues=np.zeros(numberOfVariables)
    step=np.zeros(numberOfVariables)

with open(sys.argv[1]) as inp:
    a=0
    for line in inp:
        fields=line.strip().split()
        if len(fields)!=0:
            if(re.match("x",fields[0],re.I)):
                initialValues[a]=float(fields[1])
                if(len(fields) < 3):
                    step[a]=initialValues[a]/1000
                else:
                    step[a]=float(fields[2])
                a=a+1

sys.stdout.flush()

print("job information ", scriptName, "variables", numberOfVariables, "method", method, "limit", limit, "solver", solver, "maxIter", maxIterations)
print("initial values ", initialValues)
print("step size ", step)

if(len(initialValues)!=numberOfVariables):
    print ("check the number of variables in your script!",numberOfVariables,len(initialValues))
    exit()

coordsFile=scriptName.replace(".sh",".variables")
outName=scriptName.replace(".sh",".out")

######### optimization logs
optFile=scriptName.replace(".sh",".opt")
print('optimization results will be printed in ', optFile )
sys.stdout = open(optFile, 'w')

######### let python do the magic (?)

res = minimize(energy, initialValues, method=solver, jac=gradient, options={'gtol': limit, 'disp': True, 'maxiter': maxIterations})

finalCoords=res.x
finalEnergy=energy(finalCoords)

print("final values ", finalCoords)
print("final energy ", finalEnergy)
print("final gradient ", res.jac)
#print("final distances ", constraints_atom_1(finalCoords), constraints_atom_2(finalCoords), constraints_atom_3(finalCoords))
