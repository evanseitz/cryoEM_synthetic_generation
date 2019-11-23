# README
## Required packages
- EMAN

---

## Instructions for aligning all structures
- The `4_GenMRC_eman` folder contains the `e2pdb2mrc.sh` bash script, which will generate 3D Coulomb potential maps (`.mrc`) for each structure in the *N*x*M* state space. Before running this script (via `sh e2pdb2mrc.sh`) from the command line interface (from within this same directory), you will need to alter the following depending on your needs:
  - `outFile`: the output location; only change the initial path to match your system (i.e., nothing past `/4_GenMRC_eman/`)
  - `-A`: the pixel size of the MRC (in Angstroms); preferably 1
  - `-R`: the resolution of the MRC (in Angstroms)
  - `-B`: the box size of the MRC (in voxels)  
- Running `e2pdb2mrc.sh` will generate *N*x*M* 3D Coulomb potential maps in the output folder `MRCs`

