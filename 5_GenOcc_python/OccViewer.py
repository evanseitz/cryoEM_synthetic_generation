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
imgPath = os.path.join(pyDir, 'Occ2D_1k.npy')

imgFile = np.load(imgPath) 
imshow(imgFile,interpolation='nearest',origin='lower')
plt.show()
