# README
## Cryo-EM Synthethic Continua Generation

This repository contains the software implementation for our paper **Simulation of Cryo-EM Ensembles from Atomic Models of Molecules Exhibiting Continuous Conformations** (Seitz, Acosta-Reyes, Schwander, Frank): https://www.biorxiv.org/content/10.1101/864116v1. It contains tools to apply the discussed methods to new models.

### Instructions:
This workflow has been segmented into modules (folders 1-9) that provide the ability to create branching versions of your continuum at each step, enabling direct comparison of datasets with different motions, energetics, or noise, etc. This workfow will be optimized further in later releases. Please do not rename the internal folders or alter the hierarchy, as they are referenced repeatedly in downstream scripts. Individual instructions for use of each module in this workflow are provided within its corresponding folder. 

### Required Software:
- Python
  - numpy, pylab, matplotlib, mrcfile, csv, itertools
- Chimera (https://www.cgl.ucsf.edu/chimera/)
- PyMol (https://pymol.org/2/)
- Phenix (https://www.phenix-online.org/)
- EMAN2 (https://cryoem.bcm.edu/cryoem/downloads/view_eman2_versions)
- RELION (https://github.com/3dem/relion)

All versions of the last 5 libraries should be able to process the commands used in this repository. As a reference, we used `Phenix 1.17rc5-3630`, `EMAN 2.31 final`, `PyMOL 2.3.3`, `Chimera 1.13`, and `RELION 3.0.8 (Precision: BASE=double, CUDA-ACC=single)`. Additionally, either Chimera or PyMOL can be used to generate conformational motions: both have been used here (one for CM1, another for CM2) to illustrate general use.

For Phenix and Chimera, the binaries can be directly obtained on their web page. These packages require an initial registration and are free for research purposes. 

For Pymol, the official site sells licenses (there are licenses for education https://pymol.org/edu/ and research http://pymol.org/academic) as well as providing binaries to use with them. They also provide official free binaries of a legacy 0.99 version through the sourceforge site (https://sourceforge.net/projects/pymol/files/Legacy/). The other alternative is compiling; for macOS, this can be done with MacPorts, Homebrew, etc. As well, https://www.lfd.uci.edu/~gohlke/pythonlibs/ may prove useful, as it provides wheel binaries for Windows/Linux.

RELION will need to be compiled if the binaries are not used. The pre-compiled version comes as a part of the CCPEM package suite (https://www.ccpem.ac.uk/download.php). As a note, for Windows, RELION can be compiled using Windows Subsystem Linux (WSL), but will not have access to GPU.

### Environment:
First, install Anaconda. Navigate to your project directory via the command line interface and install the environment corresponding to your operating system via:

`conda create --name synth --file env_linux_64.txt`

`conda create --name synth --file env_mac_64.txt`

(If this installation method throws any errors for your machine, we recommend installing the ManifoldEM environment instead, with corresponding instructions in the user manual located at https://github.com/evanseitz/ManifoldEM_Python)

Once the Anaconda environment is installed, it must be initiated each time before running (the majority of) these scripts via the command: `conda activate synth`. As an important note, this environment is highly particular - make sure not to install any other python packages while `synth` is active (sourced), as conflicts may emerge. When you are done using the environment, always exit via: `conda deactivate`

### Attribution:
Please cite our manuscript if you find this framework useful in your research:


	@article {Seitz_Synth_MS,
		author = {Seitz, E. and Acosta-Reyes, F. and Schwander, P. and Frank, J.},
		title = {Simulation of cryo-{E}{M} ensembles from atomic models of molecules exhibiting continuous conformations},
		year = {2019},
		doi = {10.1101/864116},
		publisher = {Cold Spring Harbor Laboratory},
		URL = {https://www.biorxiv.org/content/10.1101/864116v1},
		journal = {bioRxiv}}

Additionally, you can cite this repository code directly via the following DOI:

[![DOI](https://zenodo.org/badge/220536612.svg)](https://zenodo.org/badge/latestdoi/220536612)


### License:
Copyright 2018-2020 Evan Seitz
Frank Lab, Columbia University

For further details, please see the LICENSE file.
