import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 


J = 4
data = pd.read_csv("levels.txt", sep="\t")
energies = data["E[cm-1]"].astype("float")
energies_absK = np.unique(energies[2*J+1:])
#energies_absK = energies[2*J+1:]


dataNOCI = pd.read_csv("NOCI_Energies.txt")
energies_NOCI = dataNOCI["ENERGY[E_H]"].astype("float")
E_reference_NOCI = energies_NOCI[0]
energies_NOCI_in_CM = [(i - E_reference_NOCI)*4.55633E6 for i in energies_NOCI]



x = [1] * len(energies_absK)

x_NOCI = [1] * len(energies_NOCI_in_CM)

fig, ax = plt.subplots()
ax.scatter(x, energies_absK, s=90000, marker="_", linewidth=2, zorder=3, color = "red")
ax.scatter(x_NOCI, energies_NOCI_in_CM, s=90000, marker="_", linewidth=2, zorder=3)
ax.grid(axis='y')
ax.set_ylabel("$\\Delta E  [cm^{-1}]$")
ax.set_ylim([0,10])
plt.show()