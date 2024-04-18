#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import subprocess
import numpy as np
import time
import signal

FirstCubeFileName = sys.argv[1]
FirstCubeFile = open(FirstCubeFileName, "r" )
FirstCubeFileLines = FirstCubeFile.readlines()

# comments
commentLines = FirstCubeFileLines[0:2]

# reading box parametes
n_atoms = int(FirstCubeFileLines[2].split()[0])
origin = list(map(float,FirstCubeFileLines[2].split()[1:4]))

n_points = list()
steps = list()
for i in range (3,6 ) : 
    n_points.append (int (FirstCubeFileLines[i].split()[0]) )
    steps.append( list(map( float, (FirstCubeFileLines[i].split()[1:4]) ) ))

atoms = list()
for i in range (6,6+int(n_atoms) ) : 
    atoms.append( list(map( float, (FirstCubeFileLines[i].split()) ) ))

# printing

print("commentLines",commentLines)
print("n_atoms",n_atoms)
print("origin",origin)
print("n_points",n_points)
print("steps",steps)
print("atoms",atoms)

print( "."*20)

# reading the grid

cubeFileLines = FirstCubeFileLines[6+int(n_atoms):]
grid = np.zeros((n_points[0]*n_points[1]*n_points[2]))
i = 0
for line in cubeFileLines:
    for val in line.strip().split():
        grid[i] = float(val)
        i += 1
grid = np.reshape(grid, (n_points[0], n_points[1], n_points[2]))

FirstCubeFile.close()


############################################
##### Now we open the second cube file #####
############################################

SecondCubeFileName = sys.argv[2]
SecondCubeFile = open(SecondCubeFileName, "r" )
SecondCubeFileLines = SecondCubeFile.readlines()

# comments
scommentLines = SecondCubeFileLines[0:2]

# reading box parametes
sn_atoms = int(SecondCubeFileLines[2].split()[0])
sorigin = list(map(float,SecondCubeFileLines[2].split()[1:4]))

sn_points = list()
ssteps = list()
for i in range (3,6 ) : 
    sn_points.append (int (SecondCubeFileLines[i].split()[0]) )
    ssteps.append( list(map( float, (SecondCubeFileLines[i].split()[1:4]) ) ))

satoms = list()
for i in range (6,6+int(sn_atoms) ) : 
    satoms.append( list(map( float, (SecondCubeFileLines[i].split()) ) ))

# printing

print("commentLines",scommentLines)
print("n_atoms",sn_atoms)
print("origin",sorigin)
print("n_points",sn_points)
print("steps",ssteps)
print("atoms",satoms)

print( "."*20)

# reading the grid

SecondCubeFileLines = SecondCubeFileLines[6+int(sn_atoms):]
sgrid = np.zeros((sn_points[0]*sn_points[1]*sn_points[2]))
i = 0
for line in SecondCubeFileLines:
    for val in line.strip().split():
        sgrid[i] = float(val)
        i += 1
sgrid = np.reshape(sgrid, (sn_points[0], sn_points[1], sn_points[2]))

SecondCubeFile.close()




    

