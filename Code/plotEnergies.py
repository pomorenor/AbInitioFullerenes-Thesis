import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import sys

J = sys.argv[1]
data = pd.read_csv("levels.txt", sep="\t")
energies = data["E[cm-1]"].astype("float")
#energies_absK = np.unique(energies[2*J+1:])
energies_absK = energies


dataNOCI_duplet = pd.read_csv("energies_duplet.txt")
energies_NOCI_duplet = dataNOCI_duplet["ENERGY[E_H]"].astype("float")
E_reference_NOCI_duplet = energies_NOCI_duplet[0]
energies_NOCI_in_CM_duplet = [(i - E_reference_NOCI_duplet)*4.55633E6 for i in energies_NOCI_duplet]


dataNOCI_quartet = pd.read_csv("energies_quartet.txt")
energies_NOCI_quartet = dataNOCI_quartet["ENERGY[E_H]"].astype("float")
E_reference_NOCI_quartet = energies_NOCI_quartet[0]
energies_NOCI_in_CM_quartet = [(i - E_reference_NOCI_quartet)*4.55633E6 for i in energies_NOCI_quartet]



x = [1] * len(energies_absK)

x_NOCI_duplet = [2] * len(energies_NOCI_in_CM_duplet)
x_NOCI_quartet = [3] * len(energies_NOCI_in_CM_quartet)



fig, ax = plt.subplots()
ax.scatter(x, energies_absK, s=90000, marker="_", linewidth=2, zorder=3, color = "black")
ax.scatter(x_NOCI_duplet, energies_NOCI_in_CM_duplet, s=90000, marker="_", linewidth=2, zorder=3, color = "red")
ax.scatter(x_NOCI_quartet, energies_NOCI_in_CM_quartet, s=90000, marker="_", linewidth=2, zorder=3, color = "purple")
ax.grid(axis='y')
ax.set_ylabel("$\\Delta E  [cm^{-1}]$")
ax.set_ylim([0,500])
plt.show()