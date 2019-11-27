import os, os.path, sys
import numpy as np
import mrcfile
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import quatsGaussian

mrcPaths = []
pyDir = os.path.dirname(os.path.abspath(__file__)) #python file directory
parDir = os.path.dirname(pyDir) #parent directory
mrcDir = os.path.join(parDir, '6_GenClones_python/MRC_clones') #occupancies from non-uniform occupancy map

i = 0
for root, dirs, files in os.walk(mrcDir):
    for file in sorted(files):
        if not file.startswith('.'): #ignore hidden files
            if file.endswith(".mrc"):
                mrcPaths.append(os.path.join(root, file))
                i += 1

rotAll = []
tiltAll = []
psiAll = []

for i in mrcPaths:
    print(i)
    path = os.path.splitext(i)[0]
    state = os.path.split(path)[1] #'state_01_01', etc.
    alignOut = os.path.join(pyDir, 'STARs/proj812_%s.star' % state)
    if os.path.exists(alignOut):
        os.remove(alignOut)

    ##########################
    # import angles:
    S2 = pd.read_csv('tessellations/proj812.txt', header=None, delim_whitespace=True) #projections
    if 1: #perform quaternion perturbations on each PD
        rot, tilt = quatsGaussian.op(S2) 
        psi = S2[3] #no in-plane rotations
        
        rotAll.append(rot)
        tiltAll.append(tilt)
        psiAll.append(psi)
    else:
        rot = S2[1]
        tilt = S2[2]
        psi = S2[3]
    
    alignFile = open(alignOut, 'w')
    alignFile.write('\ndata_ \
            \n \
            \nloop_ \
            \n \
            \n_rlnAngleRot #1 \
            \n_rlnAngleTilt #2 \
            \n_rlnAnglePsi #3 \
            \n_rlnOriginX #4 \
            \n_rlnOriginY #5 \
            \n_rlnDefocusU #6 \
            \n_rlnDefocusV #7 \
            \n_rlnVoltage #8 \
            \n_rlnSphericalAberration #9 \
            \n_rlnAmplitudeContrast #10 \
            \n_rlnDefocusAngle #11 \
            \n_rlnCtfBfactor #12 \
            \n_rlnPhaseShift #13 \
            \n_rlnPixelSize #14 \
            \n')

    for i in range(0,len(rot)):
        df = np.random.randint(low=2000, high=10000, size=1)[0]
        if 1:
            x = 0
            y = 0
        else: #x-, y-shifts on object's center in each image
            x = np.random.uniform(-5,5)
            y = np.random.uniform(-5,5)

        alignFile.write('%.6f\t%.6f\t%.6f\t%.3f\t%.3f\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
            % (rot[i],tilt[i],psi[i],x,y,float(df),float(df),300.,2.7,.1,0.,0.,0.,1.))

    alignFile.close()
    


    

