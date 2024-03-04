import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 


J = 2
data = pd.read_csv("levels.txt", sep="\t")
energies = data["E[cm-1]"].astype("float")
energies_absK = np.unique(energies[2*J+1:])


x = [1] * len(energies_absK)

fig, ax = plt.subplots()
ax.scatter(x, energies_absK, s=90000, marker="_", linewidth=2, zorder=3)
ax.grid(axis='y')
plt.show()