import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.interpolate import make_interp_spline


def smooth_curve(x, y, points=500):
    x_new = np.linspace(x.min(), x.max(), points)
    spline = make_interp_spline(x, y, k=3)  # cubic spline
    y_new = spline(x_new)
    return x_new, y_new


# cube filenames
cube1 = sys.argv[1]
cube2 = sys.argv[2]
cube3 = sys.argv[3]

cubes = [cube1, cube2, cube3]
labels = ["Quartet", "Doublet alpha", "Doublet beta"]  # edit as needed

# function to load line data
def load_lines(cube_name):
    data_x = np.loadtxt(cube_name + ".X_line.dat")
    data_y = np.loadtxt(cube_name + ".Y_line.dat")
    data_z = np.loadtxt(cube_name + ".Z_line.dat")
    
    return (
        data_x[:,0], data_x[:,1],
        data_y[:,0], data_y[:,1],
        data_z[:,0], data_z[:,1]
    )

# load all cubes
datasets = [load_lines(c) for c in cubes]

# create subplots
fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharey=True)

# plot each cube
for data, label in zip(datasets, labels):
    x, rho_x, y, rho_y, z, rho_z = data
    
    x_s, rho_x_s = smooth_curve(x, rho_x)
    y_s, rho_y_s = smooth_curve(y, rho_y)
    z_s, rho_z_s = smooth_curve(z, rho_z)

    axes[0].plot(x_s, rho_x_s, label=label)
    axes[1].plot(y_s, rho_y_s, label=label)
    axes[2].plot(z_s, rho_z_s, label=label)

# titles and labels
axes[0].set_title("Density along X")
axes[1].set_title("Density along Y")
axes[2].set_title("Density along Z")

axes[0].set_xlabel("x (a.u.)")
axes[1].set_xlabel("y (a.u.)")
axes[2].set_xlabel("z (a.u.)")

for ax in axes:
    ax.set_ylabel("Density")
    ax.legend()

plt.tight_layout()
plt.show()

