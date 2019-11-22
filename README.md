# synthetic_continua
Simulation of cryo-EM ensemble data from atomic models of molecules exhibiting continuous motions.

### paper:


### required software:
- Python
  - numpy, pylab, matplotlib, mrcfile, csv, itertools
- Chimera
- PyMol
- Phenix
- EMAN2
- RELION

### environment:
First, install Anaconda. Navigate to your project directory via the command line interface and install the environment corresponding to your operating system via:

`conda create --name synth --file env_linux_64.txt`

`conda create --name synth --file env_mac_64.txt`

Once the Anaconda environment is installed, it must be initiated each time before running (the majority of) these scripts via the command: `conda activate synth`

When you are done using the environment, always exit via: `conda deactivate`

### instructions:
This repository lays out the file/folder structure needed to produce synthetic continuum datasets. Please do not rename the internal folders here, as that they are referenced by several different scripts. Individual instructions for use are provided within each subsequent module.
