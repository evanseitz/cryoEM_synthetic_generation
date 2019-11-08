import numpy as np
import matplotlib
from matplotlib import rc
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pylab import imshow, show, loadtxt, axes
import scipy
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import math


def f1(x, y):
    func1 = .5*np.sin((np.pi*(x))/21)*np.cos((3*np.pi*(y-5.5))/21)
    func2 = 2.4*np.sin((np.pi*(x))/21)*np.cos((2*np.pi*(y-5.5))/21)
    func3 = np.real((func1 + func2)**2) + 1
    return func3
    

x = np.linspace(1, 20, 20)
y = np.linspace(1, 20, 20)

X, Y = np.meshgrid(x, y, sparse=False)
Z = f1(X, Y)

if 1:
    for i in range(0,20):
        for j in range(0,20):
	    Z[i,j] = math.floor(Z[i,j])
	    if i == 4 and j == 9:
		Z[i,j] -= 1
	    if i == 4 and j == 10:
		Z[i,j] -= 1

sumZ = np.sum(Z)
#np.save('Occ2D_1k.npy', Z)

if 1: #occupancy plot
    imshow(Z,origin='lower',extent=[1,20,1,20],interpolation='nearest')
    plt.colorbar()
    plt.title('2D Occupancy Map')
    #plt.title('Total Occupancy / PD: %s' % int(sumZ))
    plt.xlabel('Conformational Coordinate 1', fontsize=12)
    plt.ylabel('Conformational Coordinate 2', fontsize=12)
    plt.show()

E = np.ndarray(shape=(20,20), dtype=float)
occmax = np.amax(Z)
for i in range(0,20):
    for j in range(0,20):
        E[i,j] = -np.log((float(Z[i,j])/float(occmax)))
if 0: #2d energies          
    imshow(E,origin='lower',extent=[1,20,1,20],interpolation='nearest')
    cbar = plt.colorbar()
    cbar.ax.set_title('kcal/mol')#, rotation=270)
    plt.title('2D Energy Landscape')
    plt.xlabel('Conformational Coordinate 1', fontsize=12)
    plt.ylabel('Conformational Coordinate 2', fontsize=12)
    plt.show()

if 0: #1d energy projections
    CC1 = []
    for i in range(0,20):
        CC1.append(sum(Z[:,i])) #CC1
    CC2 = []
    for i in range(0,20):
        CC2.append(sum(Z[i,:])) #CC2
    
    plt.plot(range(1,21),CC1, label='CC1')
    plt.plot(range(1,21),CC2, label='CC2')

    plt.ylabel('Occupancy')
    plt.xlabel('Conformational Coordinates')
    plt.xlim([1,20])
    plt.yticks([20,30,40,50,60,70,80,90,100])
    plt.title('1D Occupancy Maps')
    plt.legend()
    plt.show()
    
