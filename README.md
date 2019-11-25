# README
## Simulation of cryo-EM ensemble data from atomic models of molecules exhibiting continuous motions

### Abstract:
Molecular machines visit a continuum of conformational states as they go through work cycles required for their metabolic functions. Single-molecule cryo-EM of suitable in vitro systems affords the ability to collect a large ensemble of projections depicting the continuum of structures and assign occupancies, or free energies, to the observed states. Through the use of machine learning and dimension reduction algorithms it is possible to determine a low-dimensional free energy landscape from such data, allowing the basis for molecular function to be elucidated. In the absence of ground truth data, testing and validation of such methods is quite difficult, however. In this work, we propose a workflow for generating simulated cryo-EM data from an atomic model subjected to conformational changes. As an example, an ensemble of structures and their multiple projections was created from heat shock protein Hsp90 with two defined conformational degrees of freedom.

**Link:**

---

### Instructions:
This repository lays out the file/folder structure needed to produce customized synthetic continuum datasets. This workflow has been segmented into modules (folders 1-9) that provide the ability to create branching versions of your continuum at each step to compare (e.g., datasets of the same structure but with different motions, energetics, or noise). This workfow will be optimized further in later releases. Please do not rename the internal folders here, as that they are referenced by several different scripts. Individual instructions for use of each module in this workflow are provided within the corresponding folder. 

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

