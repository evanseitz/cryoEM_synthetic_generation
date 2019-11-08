import os, os.path, sys
import numpy as np
import mrcfile
import pandas as pd

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

for i in mrcPaths:
    path = os.path.splitext(i)[0]
    state = os.path.split(path)[1] #'state_01_01', etc.
    alignOut = os.path.join(pyDir, 'STARs/proj812_%s.star' % state)
    if os.path.exists(alignOut):
        os.remove(alignOut)

    ##########################
    # import angles:
    angles = pd.read_csv('proj812.txt', header=None, delim_whitespace=True) #projections
    rot = angles[1]
    tilt = angles[2]
    psi = angles[3]

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
            \n')

    for i in range(0,len(rot)):  
        df = np.random.randint(low=4000, high=12000, size=1)[0]
        #df = 0
        #x = np.random.uniform(-5,5)
        #y = np.random.uniform(-5,5)
        x = 0
        y = 0

        alignFile.write('%.6f\t%.6f\t%.6f\t%.3f\t%.3f\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
            % (rot[i],tilt[i],psi[i],x,y,float(df),float(df),300.,2.7,.1,0.,0.,0.))

    alignFile.close()
