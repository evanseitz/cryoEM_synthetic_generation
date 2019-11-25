# README
## 

This repository contains the software implementation for our paper *Simulation of cryo-EM ensemble data from atomic models of molecules exhibiting continuous motions* (Seitz, Acosta-Reyes, Schwander, Frank), bioRxiv:. It contains tools to apply the discussed methods to new models.

This workflow has been segmented into modules (folders 1-9) that provide the ability to create branching versions of your continuum at each step, enabling direct comparison of datasets with different motions, energetics, or noise, etc. This workfow will be optimized further in later releases. Please do not rename the internal folders or alter the hierarchy, as they are referenced repeatedly in downstream scripts. Individual instructions for use of each module in this workflow are provided within its corresponding folder. 

### Required Software:
- Python
  - numpy, pylab, matplotlib, mrcfile, csv, itertools
- Chimera
- PyMol
- Phenix
- EMAN2
- RELION

### Environment:
First, install Anaconda. Navigate to your project directory via the command line interface and install the environment corresponding to your operating system via:

`conda create --name synth --file env_linux_64.txt`

`conda create --name synth --file env_mac_64.txt`

Once the Anaconda environment is installed, it must be initiated each time before running (the majority of) these scripts via the command: `conda activate synth`

When you are done using the environment, always exit via: `conda deactivate`

### Attribution:
Please cite `E. Seitz, F. Acosta-Reyes, P. Schwander and J. Frank (2019) <http:biorxiv.org///>` if you find this code useful in your research.

### License:
Copyright 2018-2019 Evan Seitz
For further details, please see the LICENSE file.
