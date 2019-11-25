import os, os.path, sys
import numpy as np
import itertools
import matplotlib
import matplotlib.pyplot as plt
from pylab import imshow, show, loadtxt
import mrcfile
import csv
import re

# required environment = ManifoldEM
matlab = False

##########################
# user inputs:
pyDir = os.path.dirname(os.path.abspath(__file__)) #python file directory
parDir = os.path.dirname(pyDir) #parent directory

dataDir = os.path.join(parDir, '8_GenStacksCTF_relion/stacks') #location of all .star and .mrcs

stackOut = os.path.join(pyDir, 'Hsp2D_5PD.mrcs')
alignOut = os.path.join(pyDir, 'Hsp2D_5PD.star')
if os.path.exists(stackOut):
    os.remove(stackOut)
if os.path.exists(alignOut):
    os.remove(alignOut)

if matlab:
    binaryOut = os.path.join(pyDir, 'Hsp2D_5PD.dat')
    spiderOut = os.path.join(pyDir, 'Hsp2D_5PD.spi')
    if os.path.exists(spiderOut):
        os.remove(spiderOut)
    if os.path.exists(binaryOut):
        os.remove(binaryOut)
    
occFile = os.path.join(parDir, '5_GenOcc_python/Occ2D_1k.npy')
occ = np.load(occFile)
temp_stack = mrcfile.open(os.path.join(dataDir, 'state_01_01_1.mrcs'))
PDs, box, box = temp_stack.data.shape
#temp_stack.close
PDs = 5 #comment out for full stack
snapshots = int(np.sum(occ)*PDs)
print('Snapshots:',snapshots)

starPaths = []
i = 0
for root, dirs, files in os.walk(dataDir):
    for file in sorted(files):
        if not file.startswith('.'): #ignore hidden files
            if file.endswith(".star"):
                starPaths.append(os.path.join(root, file))
                i += 1

stackPaths = []
i = 0
for root, dirs, files in os.walk(dataDir):
    for file in sorted(files):
        if not file.startswith('.'): #ignore hidden files
            if file.endswith(".mrcs"):
                stackPaths.append(os.path.join(root, file))
                i += 1
    
##########################
# FUNCTIONS:
##########################
# function to find SNR:
def find_SNR(image):
    pixFreq2d = []
    for a in image:
        pixFreq2d.append(a)
    pixFreq1d = list(itertools.chain.from_iterable(pixFreq2d))
    sig_mean = np.mean(pixFreq1d)
    sig_var = np.var(pixFreq1d)
    noise_var = sig_var / 0.1 #experimental regime
    noise_std = np.sqrt(noise_var)
    return sig_mean, noise_std

##########################
# function to add noise:
def add_noise(mean, std, image):
    row, col = image.shape
    gauss = np.random.normal(mean, std, (row, col))
    gauss = gauss.reshape(row, col)
    noisy = image + gauss
    return noisy

##########################
# function to normalize:
def normalize(image):
    bg = []
    h, w = image.shape[:2]
    center = [int(w/2), int(h/2)]
    radius = int(h/2)
    Y, X = np.ogrid[:h,:w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y - center[1])**2)
    mask = dist_from_center <= radius
    masked_img = image.copy()
    if 0: #for visualization of mask only, keep off (0)
        masked_img[~mask] = 0
        plt.imshow(masked_img, cmap='gray')
        plt.show()
    bg = masked_img[~mask]
    bg_mean = np.mean(bg)
    bg_std = np.std(bg)
    img_norm = (image - bg_mean) / bg_std
    if 0: #NORM CHECK, for testing only
        print('bg_mean:', bg_mean)
        print('bg_std:',bg_std)
    return img_norm

##########################
# PREPROCESSING:
##########################

# initiate alignment file:
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
                \n_rlnImageName #15 \
                \n')

# initiate spider file:
if matlab:
    spiderFile = open(spiderOut, 'w')

##########################
# create empty arrays:
img_array = mrcfile.new_mmap(stackOut, shape=(snapshots,box,box), mrc_mode=2, overwrite=True) #mrc_mode 2: float32
if matlab:
    binary_array = np.memmap(binaryOut, dtype='float32', mode='w+', shape=(snapshots,box,box))#, offset=4*box**2)

##########################
# INITIATE MAIN LOOP:
##########################
# import original stacks:
idx = 0 #index for stack/stars
img = 0 #index for every individual image in new stack
for z in stackPaths:
    stack = mrcfile.open(z)
    starPath = starPaths[idx]
        
    starFile = []
    with open(starPath, 'r') as values: 
        for i in range(0,19): #skip header
            next(values)
        starReader = csv.reader(values)
        for lines in starReader:
            starFile.append(lines)
    values.close()

    #for PD in range(len(stack.data)): #e.g., [0,812]
    for PD in [93, 194, 267, 469, 533]: #comment out for full stack and use above line instead
        img_orig = stack.data[PD] #each image within a given stack; e.g. len = 812

        sig_mean, noise_std = find_SNR(img_orig) #find SNR
        img_noise = add_noise(sig_mean, noise_std, img_orig) #apply noise
        img_norm = normalize(img_noise) #normalize
        
        img_array.data[img] = img_norm
        if matlab:
            ary_array[img] = img_norm

        #print('norm check:')
        #normalize(img_norm) #NORM CHECK

        #############################
        # update alignment file:
        star = re.split(r'[ ,|;"]+', starFile[PD+1][0]) #need to make sure skipping header correctly
        alignFile.write('%.6f\t%.6f\t%.6f\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s@Hsp2D_5PD.mrcs\n' \
            % (float(star[1]), float(star[2]), float(star[3]), float(star[4]), float(star[5]), \
            float(star[6]), float(star[7]), float(star[8]), float(star[9]), float(star[10]), \
            float(star[11]), float(star[12]), float(star[13]), float(star[14]), img+1))
	
	# update spider file (index, number of params, psi, theta [0,180], phi [-180,180], class, x, y, u, v, uv angle):
	if matlab:
	    spiderFile.write('%s\t%s\t%.6f\t%.6f\t%.6f\t%s\t%s\t%s\t%s\t%s\t%s\n' \
	      % (img+1, 9, float(star[3]), float(star[2]), float(star[1])-180, 1, 0, 0, float(star[6]), float(star[7]), 0))
        
        img += 1
        print('%s / %s' % (img, snapshots))

    idx += 1
    stack.close()
    
alignFile.close()
if matlab:
    spiderFile.close()
    
print('All Processes Complete')
