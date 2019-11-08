import os, os.path, sys
import shutil
import numpy as np
import cv2
import itertools
import matplotlib
import matplotlib.pyplot as plt
from pylab import imshow, show, loadtxt
import mrcfile
from scipy.fftpack import ifftshift
from scipy.fftpack import fft2
from scipy.fftpack import ifft2
import csv
import pandas as pd

# required environment = ManifoldEM

##########################
# user inputs:
pyDir = os.path.dirname(os.path.abspath(__file__)) #python file directory
parDir = os.path.dirname(pyDir) #parent directory
origDir = os.path.join(parDir, '4_GenMRC_eman/MRCs')
occPath = os.path.join(parDir, '5_GenOcc_python/Occ2D_1k.npy')
cloneDir = os.path.join(parDir, '6_GenMRC_pyClones/MRC_clones')

occFile = np.load(occPath)
states = 20

occ = []
for i in range(1, states+1): #[1,20]
    for j in range(1, states+1): #[1,20]
        occ.append(occFile[j-1][i-1])
	
occMax = int(np.amax(occ))
	
fnames = []
for filename in os.listdir(origDir):
    if filename.endswith('.mrc'):
        fnames.append(filename)
fnames.sort(key=lambda f: int(filter(str.isdigit, f)))

idx = 0
for i in fnames:
    shutil.copy('%s/%s' % (origDir,i), '%s/%s' % (cloneDir,i))
    for j in range(2,occMax+1):
	if occ[idx] >= j:
	    short = i[:-5]
	    new = short + ('%d.mrc' % j)
	    shutil.copy('%s/%s' % (origDir,i), '%s/%s' % (cloneDir,new))
    idx += 1
