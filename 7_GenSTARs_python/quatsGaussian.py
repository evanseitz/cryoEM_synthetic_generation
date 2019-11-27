import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
from math import acos, atan, atan2

# quaternion: scalar (w) + 3-vector (xi,yi,zi) -> (w,x,y,z)

def normalize(v, tolerance=0.00001): #normalize to space of unit quaternions
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance: #magnitude should be ~ 1
        mag = np.sqrt(mag2)
        v = tuple(n / mag for n in v)
    return v

# every rotation represented by a unit vector
#concatenations of rotations correspond to multiplications of unit quaternions:
def q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z

def q_conjugate(q): #to rotate vector by quat, need quat's conjugate too
    w, x, y, z = q
    return (w, -x, -y, -z)

# quat-vector multiplication: convert a vector in a quat (by setting w=0, leave x,y,z same),
#then multiply q*v*q_conjugate(q):
def qv_mult(q1, v1):
    q2 = (0.0,) + v1
    return q_mult(q_mult(q1, q2), q_conjugate(q1))[1:]

# convert from axis-angle rotations to quaternions:
def axisangle_to_q(v, theta):
    v = normalize(v)
    x, y, z = v
    theta /= 2
    w = np.cos(theta)
    x = x * np.sin(theta)
    y = y * np.sin(theta)
    z = z * np.sin(theta)
    return w, x, y, z

# and back:
def q_to_axisangle(q):
    w, v = q[0], q[1:]
    theta = acos(w) * 2.0
    return normalize(v), theta

# find orthonormal components for a given vector:
def orthonormal(k):
    x = (k[1],-k[0],0)
    length = np.sqrt(k[0]**2 + k[1]**2)
    if length > 1e-15:
        x = x/length
    else:
        x = (1,0,0) #handle exceptions for k = (0,0,1) and k = (0,0,-1)
    
    if 0: #sanity-check
        print('x:', x)
        print('norm x:', np.linalg.norm(x))
        print('x dot k:', np.dot(x,k))
    return x    

# convert final unit-vectors to Euler:
def cart2sph(x, y, z): 
    r = np.sqrt(x**2 + y**2 + z**2)
    phi = atan2(y,x)*180./np.pi
    theta = acos(z/r)*180./np.pi
    return (r, phi, theta)

##################################
# example of use:
if 0:
    x_axis_unit = (1, 0, 0)
    y_axis_unit = (0, 1, 0)
    z_axis_unit = (0, 0, 1)
    r1 = axisangle_to_q(x_axis_unit, np.pi / 2)
    r2 = axisangle_to_q(y_axis_unit, np.pi / 2) 
    r3 = axisangle_to_q(z_axis_unit, np.pi / 2)
    #recall: right-hand-rule
    v = qv_mult(r1, y_axis_unit) #y shifts by 90deg CW about x-axis: [0,0,1]
    print('pos after 1st rot:', v)
    v = qv_mult(r2, v) #y' at [0,0,1] rotates 90deg CW about y-axis: [1,0,0]
    print('pos after 2nd rot:', v)
    v = qv_mult(r3, v) #y'' goes back to its original location: [0,1,0]
    print('pos after 3rd rot:', v)
##################################

def op(S2):
    ######################   
    # load in PD vectors:
    x0 = S2[4]
    y0 = S2[5]
    z0 = S2[6]
    PDs = np.ndarray(shape=((len(x0),3)), dtype=float)
    idx = 0
    for xyz in range(len(x0)):
        PDs[idx] = [x0[idx], y0[idx], z0[idx]]
        idx += 1
    #####################################   
    # apply random angular perturbations:
    cartesian = [] #final positions of each rotated PD
    rot = [] #i.e., phi (or azimuthal)
    tilt = [] #i.e., theta (or elevation)
    for k in PDs:
        k = k / (k**2).sum()**0.5 #normalize initial vector
        x = orthonormal(k) #find orthonormal component of k
        
        w1 = np.random.normal(0, np.pi/144, 1) #mu, sigma (in radians), number of samples
        r1 = axisangle_to_q(x, w1) #rotate about x by w1 degrees 
        k1 = qv_mult(r1, (k[0],k[1],k[2])) #rotate k about x
        
        w2 = np.random.uniform(-np.pi,np.pi,1) #full circle of options
        r2 = axisangle_to_q(k, w2)
        k2 = qv_mult(r2, (k1[0],k1[1],k1[2])) #rotate v1 about k
        
        cartesian.append(k2)
        r, phi, theta = cart2sph(k2[0], k2[1], k2[2]) #convert cartesian coords to spherical
        rot.append(float(phi)+180.)
        tilt.append(float(theta))
    
    ###################
    # plot data:
    if 0:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_aspect('equal')
        ax.plot([0,0,0],[1,0,0],c='k')
        ax.plot([0,0,0],[-1,0,0],c='k')
        ax.plot([0,1,0],[0,0,0],c='k')
        ax.plot([0,-1,0],[0,0,0],c='k')
        ax.set_xlim(-1,1)
        ax.set_ylim(-1,1)
        ax.set_zlim(-1,1)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ###################
        # draw unit-sphere
        uu, vv = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        xx = np.cos(uu)*np.sin(vv)
        yy = np.sin(uu)*np.sin(vv)
        zz = np.cos(vv)
        ax.plot_wireframe(xx, yy, zz, color="lightgray")
        ###################
        for i in PDs:
            ax.scatter(i[0], i[1], i[2], s=10, linewidth=0, c='k')#,c=np.random.rand(3,))
        for i in cartesian:
            ax.scatter(i[0], i[1], i[2], c='cyan', s=10, linewidth=.5)
        plt.show()
        
    return rot, tilt


if __name__ == '__main__':
    S2 = pd.read_csv('proj812.txt', header=None, delim_whitespace=True) #projection directions
    op(S2)

