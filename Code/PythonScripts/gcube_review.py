#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import subprocess
import numpy as np
import time
import signal

cubeFileName = sys.argv[1]
cubeFile = open(cubeFileName, "r" )
cubeFileLines = cubeFile.readlines()

# comments
commentLines = cubeFileLines[0:2]

# reading box parametes
n_atoms = int(cubeFileLines[2].split()[0])
origin = list(map(float,cubeFileLines[2].split()[1:4]))

n_points = list()
steps = list()
for i in range (3,6 ) : 
    n_points.append (int (cubeFileLines[i].split()[0]) )
    steps.append( list(map( float, (cubeFileLines[i].split()[1:4]) ) ))

atoms = list()
for i in range (6,6+int(n_atoms) ) : 
    atoms.append( list(map( float, (cubeFileLines[i].split()) ) ))

# printing

print("commentLines",commentLines)
print("n_atoms",n_atoms)
print("origin",origin)
print("n_points",n_points)
print("steps",steps)
print("atoms",atoms)

print( "."*20)

# reading the grid

cubeFileLines = cubeFileLines[6+int(n_atoms):]
grid = np.zeros((n_points[0]*n_points[1]*n_points[2]))
i = 0
for line in cubeFileLines:
    for val in line.strip().split():
        grid[i] = float(val)
        i += 1
grid = np.reshape(grid, (n_points[0], n_points[1], n_points[2]))

cubeFile.close()

# norm check
print("norm check", grid.sum()*steps[0][0]*steps[1][1]*steps[2][2] )

# distanceCheck
normCheck=0
expectedDistance=0
cutoff=[]
cutoff.append(0.001)
cutoff.append(0.01)
cutoff.append(0.1)
cutoff.append(0.002)
cutoff.append(0.02)
cutoff.append(0.2)
cutoff.append(0.03)
cutoff.append(0.04)
cutoff.append(0.044)
cutoff.append(0.06)
cutoff.append(0.18)
cutoff.append(0.24)
cutoff.append(0.264)
contourDens=np.zeros(len(cutoff))

for i in range(0,n_points[0]) :
    for j in range(0,n_points[1]) :
        for k in range(0,n_points[2]) :
            r=np.sqrt((origin[0] + steps[0][0]*i)**2+(origin[1] + steps[1][1]*j)**2+(origin[2] + steps[2][2]*k)**2)
            normCheck+= grid[i,j,k]
            expectedDistance+= grid[i,j,k]*r
            for n in range(len(cutoff)):
                if(grid[i,j,k]>cutoff[n]):
                    contourDens[n]+=grid[i,j,k]

print("expeced Distance", expectedDistance*steps[0][0]*steps[1][1]*steps[2][2] )
print("norm check", normCheck*steps[0][0]*steps[1][1]*steps[2][2] )

print("contourValue", "density fraction" )
for n in range(len(cutoff)):
    print(cutoff[n],contourDens[n]/normCheck)

 

FileName_2D = cubeFileName + ".YZ.dat"
File_2D = open(FileName_2D, "w" )

axis_1 = 1 # 0:x, 1:y, 2:z
axis_2 = 2 # 0:x, 1:y, 2:z
cut = [0.0,0.0]

for i in range(0,n_points[axis_1]) :
    for j in range(0,n_points[axis_2]) :
        a = int ((cut[0] - origin[0] ) / steps[0][0] )
        File_2D.write( "%.4f %.4f %.8e \n" % (  origin[0] + steps[1][1]*i, origin[1] + steps[2][2]*j, grid[a,i,j] ))
    File_2D.write( "\n")
File_2D.close()

FileName_2D = cubeFileName + ".XZ.dat"
File_2D = open(FileName_2D, "w" )

axis_1 = 0 # 0:x, 1:y, 2:z
axis_2 = 2 # 0:x, 1:y, 2:z
cut = [0.0,0.0]

for i in range(0,n_points[axis_1]) :
    for j in range(0,n_points[axis_2]) :
        a = int ((cut[0] - origin[1] ) / steps[1][1] )
        File_2D.write( "%.4f %.4f %.8e \n" % (  origin[0] + steps[0][0]*i, origin[1] + steps[2][2]*j, grid[i,a,j] ))
    File_2D.write( "\n")
File_2D.close()

FileName_2D = cubeFileName + ".XY.dat"
File_2D = open(FileName_2D, "w" )

axis_1 = 0 # 0:x, 1:y, 2:z
axis_2 = 1 # 0:x, 1:y, 2:z
cut = [0.0,0.0]

for i in range(0,n_points[axis_1]) :
    for j in range(0,n_points[axis_2]) :
        a = int ((cut[0] - origin[2] ) / steps[2][2] )
        File_2D.write( "%.4f %.4f %.8e \n" % (  origin[0] + steps[0][0]*i, origin[1] + steps[1][1]*j, grid[i,j,a] ))
    File_2D.write( "\n")
File_2D.close()


 


    

