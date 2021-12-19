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

# this version was used in https://www.biorxiv.org/content/10.1101/2021.06.18.449029v2
                
                
'''def gaus2d(x=0, y=0, mx=10.5, my=10.5, sx=4.5, sy=4.5, bg=1):
    func0 = 10
    func1 = (x - mx)**2. / (2. * sx**2.)
    func2 = (y - my)**2. / (2. * sy**2.)
    return ((func0 * np.exp(-(func1 + func2))) + bg)'''

if 1: #render with LaTeX font for figures
    rc('text', usetex=True)
    rc('font', family='serif')
                
def f1(x, y):
    func1 = np.sin((np.pi*(x))/21)*np.cos((3*np.pi*(y-5.5))/21)
    func2 = 3.025*np.sin((np.pi*(x))/21)*np.cos((2*np.pi*(y-5.5))/21)#4
    func3 = np.real((func1 + func2)**2) + 1
    return func3
    
x = np.linspace(1, 20, 20)
y = np.linspace(1, 20, 20)

X, Y = np.meshgrid(x, y, sparse=False)
Z = f1(X, Y)
Z += int(6)


np.random.seed(19680803)
if 1:
    for i in range(0,20):
        for j in range(0,20):
            if np.random.randint(3, size=1) == 0:
                Z[i,j] += 1
            elif np.random.randint(3, size=1) == 1:
                Z[i,j] -= 1
            Z[i,j] = math.floor(Z[i,j])
            if i == 4 and j == 9:
                Z[i,j] += 1
            if i == 4 and j == 10:
                Z[i,j] += 1
            if i == 14 and j == 9:
                Z[i,j] -= 2
            if i == 13 and j == 11:
                Z[i,j] -= 2

sumZ = np.sum(Z)
print(sumZ)
Z=Z.T

np.save('Occ2D_4k.npy', Z)

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
    
CC1 = []
for i in range(0,20):
    CC1.append(sum(Z[:,i])) #CC1
CC2 = []
for i in range(0,20):
    CC2.append(sum(Z[i,:])) #CC2

if 0: #1d energy projections
    plt.plot(range(1,21),CC1, label='CC1')
    plt.plot(range(1,21),CC2, label='CC2')
    plt.ylabel('Occupancy')
    plt.xlabel('Conformational Coordinates')
    plt.xlim([1,20])
    #plt.yticks([20,30,40,50,60,70,80,90,100])
    plt.title('1D Occupancy Maps')
    plt.legend()
    plt.show()
    

if 0: #OccMap, all in one plot:
    def scatter_hist(x, y, ax, ax_xBar, ax_yBar):
        # no labels
        ax_xBar.tick_params(axis="x", labelbottom=False)
        ax_yBar.tick_params(axis="y", labelleft=False)
        
        centers = [1,20,1,20]
        dx, = np.diff(centers[:2])/(X.shape[1]-1)
        dy, = -np.diff(centers[2:])/(X.shape[0]-1)
        extent = [centers[0]-dx/2, centers[1]+dx/2, centers[2]+dy/2, centers[3]-dy/2]
    
        im = ax.imshow(Z,origin='lower',extent=extent,interpolation='nearest')
        ax.set_xticks(np.arange(centers[0], centers[1]+dx, dx))
        ax.set_yticks(np.arange(centers[3], centers[2]+dy, dy))
        
        if 0:
            from mpl_toolkits.axes_grid1 import make_axes_locatable
            divider = make_axes_locatable(ax)
            cax = divider.append_axes('bottom', size='5%', pad=0.5)
            fig.colorbar(im, cax=cax, orientation='horizontal')
        
        for index, label in enumerate(ax.xaxis.get_ticklabels()):
            if index not in [0,4,9,14,19]:
                label.set_visible(False)
                
        for index, label in enumerate(ax.yaxis.get_ticklabels()):
            if index not in [0,5,10,15,19]:
                label.set_visible(False)

        ax_xBar.bar(range(1,21), CC1)
        ax_yBar.barh(range(1,21), CC2)
        
        ax_xBar.set_xlabel('Conformational Motion 1', rotation=0, labelpad=5, size=14)
        ax_yBar.set_ylabel('Conformational Motion 2', rotation=270, labelpad=15, size=14)
        ax_yBar.yaxis.set_label_position("right")
        ax_xBar.xaxis.set_label_position("top")
        
    fig = plt.figure(figsize=(8, 8))
    gs = fig.add_gridspec(2, 2,  width_ratios=(7, 2), height_ratios=(2, 7),
                          left=0.1, right=0.9, bottom=0.1, top=0.9,
                          wspace=0.05, hspace=0.05)
    ax = fig.add_subplot(gs[1, 0])
    ax_xBar = fig.add_subplot(gs[0, 0], sharex=ax)
    ax_yBar = fig.add_subplot(gs[1, 1], sharey=ax)
    scatter_hist(x, y, ax, ax_xBar, ax_yBar)
    plt.show()
    
    
'''Z = E
CC1 = []
for i in range(0,20):
    CC1.append(sum(Z[:,i])) #CC1
CC2 = []
for i in range(0,20):
    CC2.append(sum(Z[i,:])) #CC2
    
if 1: #ELS, all in one plot:
    def scatter_hist(x, y, ax, ax_xBar, ax_yBar):
        # no labels
        ax_xBar.tick_params(axis="x", labelbottom=False)
        ax_yBar.tick_params(axis="y", labelleft=False)
        
        centers = [1,20,1,20]
        dx, = np.diff(centers[:2])/(X.shape[1]-1)
        dy, = -np.diff(centers[2:])/(X.shape[0]-1)
        extent = [centers[0]-dx/2, centers[1]+dx/2, centers[2]+dy/2, centers[3]-dy/2]
    
        im = ax.imshow(Z,origin='lower',extent=extent,interpolation='nearest', cmap='magma')
        ax.set_xticks(np.arange(centers[0], centers[1]+dx, dx))
        ax.set_yticks(np.arange(centers[3], centers[2]+dy, dy))
        
        if 1:
            from mpl_toolkits.axes_grid1 import make_axes_locatable
            divider = make_axes_locatable(ax)
            cax = divider.append_axes('bottom', size='5%', pad=0.5)
            fig.colorbar(im, cax=cax, orientation='horizontal')
        
        for index, label in enumerate(ax.xaxis.get_ticklabels()):
            if index not in [0,4,9,14,19]:
                label.set_visible(False)
                
        for index, label in enumerate(ax.yaxis.get_ticklabels()):
            if index not in [0,5,10,15,19]:
                label.set_visible(False)

        ax_xBar.bar(range(1,21), CC1)
        ax_yBar.barh(range(1,21), CC2)
        
        ax_xBar.set_xlabel('Conformational Motion 1', rotation=0, labelpad=5, size=14)
        ax_yBar.set_ylabel('Conformational Motion 2', rotation=270, labelpad=15, size=14)
        ax_yBar.yaxis.set_label_position("right")
        ax_xBar.xaxis.set_label_position("top")
        
    fig = plt.figure(figsize=(8, 8))
    gs = fig.add_gridspec(2, 2,  width_ratios=(7, 2), height_ratios=(2, 7),
                          left=0.1, right=0.9, bottom=0.1, top=0.9,
                          wspace=0.05, hspace=0.05)
    ax = fig.add_subplot(gs[1, 0])
    ax_xBar = fig.add_subplot(gs[0, 0], sharex=ax)
    ax_yBar = fig.add_subplot(gs[1, 1], sharey=ax)
    scatter_hist(x, y, ax, ax_xBar, ax_yBar)
    plt.show()'''
