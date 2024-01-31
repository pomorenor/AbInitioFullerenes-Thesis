import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv("dataParams.txt", sep = "\t")
gridInfo = pd.read_csv("GRIDENERGIES.txt", sep = "\t")


angle = data["ANGLE"].astype(float)
mindist = data["MINDIST"].astype(float)
maxdist = data["MAXDIST"].astype(float)

gridnumpoints = gridInfo["GRIDPOINTS"].astype(int)
energies = gridInfo["ENERGY"].astype(float)

plt.figure()
#plt.plot(angle, mindist, label = "Minimum distance", color = "orange")
#plt.plot(angle, maxdist, label = "Maximum distance", color = "green")
#plt.axvline(x = 1.95, color = "black", linestyle = "dashed", label = "Optimal parameters")
#plt.xlabel("$\\theta  [rads]$")
#plt.ylabel("Distance $[Å]$")
plt.legend(loc = "lower left")
plt.grid()
plt.scatter(gridnumpoints, energies)
plt.xlabel("Number of grid points")
plt.ylabel("Energy $E_H$")
plt.show()
