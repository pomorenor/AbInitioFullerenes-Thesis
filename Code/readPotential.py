import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D  
import sys 


def GTF(r, centers, exponents, coefficients):

    N = coefficients.size
    function_value = 0.0

    for ii in range(0,N):

        diff = r - centers[ii]
        function_value += coefficients[ii]*np.exp(-exponents[ii]*np.dot(diff,diff))
    
    return function_value


#### First we read the name of the potential file ###
pot_file_name = sys.argv[1]


### Now we open the potential and process the info  ### 
potFile = open(pot_file_name, 'r')
lines = potFile.readlines()

num_gaussians = int(lines[2])
gauss_info_start = 3
angular_momentum = np.zeros(num_gaussians, dtype = int )
exponents = np.zeros(num_gaussians, dtype = float)
coefficients = np.zeros(num_gaussians, dtype=float)
centers = np.zeros((num_gaussians,3),dtype=float)

ii = 0
for jj in range(0, num_gaussians):
    
    angular_momentum[jj] = lines[gauss_info_start+ii].strip().split()[1]
    exponents[jj] = lines[gauss_info_start+ii+1].strip().split()[0]
    coefficients[jj] = lines[gauss_info_start+ii+1].strip().split()[1]
    
    for kk in range(0,3):
        centers[jj][kk] = lines[gauss_info_start+ii+2].strip().split()[kk]

    ii+=3



### Now we want to reducethe distances ###

R= np.linalg.norm(centers[0])
print(R)
delta = 5.0
scale = 0.9
new_centers = scale*centers




coords = np.array(centers)
new_coords = np.array(new_centers)

x = coords[:, 0]
y = coords[:, 1]
z = coords[:, 2]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(x, y, z, color = "blue")
ax.scatter(new_coords[:,0], new_coords[:,1], new_coords[:,2], color = "red")


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


r = np.array([[0, 0, z] for z in np.linspace(0, 2, 40)])

func = np.array([GTF(ri, centers, exponents, coefficients) for ri in r])
red_func = np.array([GTF(ri, new_centers, exponents, coefficients) for ri in r])

plt.plot(r[:,2], func, color = "blue")
plt.plot(r[:,2], red_func, color = "red")

plt.show()

############################################################
###Now we will write the new distances to a new potential###
############################################################


new_pot_file_name = sys.argv[2]


newPotFile = open(new_pot_file_name, 'w')

newPotFile.write(lines[0])
newPotFile.write(lines[1])
newPotFile.write(lines[2])

for ii in range(0,num_gaussians):
    newPotFile.write(str(ii)+" "+str(angular_momentum[ii])+"\n")
    newPotFile.write('\t'+str(exponents[ii])+'\t'+str(coefficients[ii])+"\n")
    newPotFile.write('\t'+str(new_centers[ii][0])+'\t'+str(new_centers[ii][1])+'\t'+str(new_centers[ii][1])+"\n")

