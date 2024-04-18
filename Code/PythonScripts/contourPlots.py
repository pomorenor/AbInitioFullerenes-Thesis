import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
import scipy.ndimage as ndimage

## We load the diles 
data_to_plot = pd.read_csv("../NOCILevel/He3-C60-1S1P1D-170-gridpoints-doublet.HE-ATOM2.dens.cub.XZ.dat", sep = " ", header=None)

i1 = data_to_plot.iloc[:, 0]
i2 = data_to_plot.iloc[:, 1]
fi1i2 = data_to_plot.iloc[:, 2]


x_grid, y_grid = np.meshgrid(np.unique(i1),np.unique(i2))
z_grid = fi1i2.values.reshape(x_grid.shape)


Z2 = ndimage.gaussian_filter(z_grid, sigma=1.0, order=0)


#plt.figure()
#plt.contour(x_grid, y_grid, z_grid )
#plt.imshow(z_grid, extent=[i1.min(), i1.max(), i2.min(), i2.max()], origin='lower', cmap='viridis',interpolation="gaussian")
#plt.show()

fig, ax = plt.subplots(3,3)
densmap = ax.imshow(Z2, extent=[i1.min(), i1.max(), i2.min(), i2.max()], origin='lower', cmap='viridis',interpolation="gaussian")
contours = ax.contour(x_grid, y_grid, Z2)
fig.colorbar(densmap, ax=ax)
plt.show()