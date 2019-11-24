# README
## Required packages
- Python
- Anaconda with `synth` environment activated (see main repository README)

---

## Instructions for aligning all structures
- The `6_GenClones_python` folder contains the `createClones.py` script, which will create duplicates of your Coulomb potential maps (`.mrc`) to match the numbers in the previously generated occupancy map. Before running this script (via `python createClones.py`) from the command line interface (from within this same directory), you will need to alter the following depending on your needs:
  - `occPath`: ensure the file path matches the occupancy map (`.npy`) generated in the previous step
  - `states`: must match the number of states used; if *N* and *M* differ, the `i, j` loop must be revised to account for this asymmetry
- Running `createClones.py` will create duplicates of your Coulomb potential maps (`.mrc`) in the `MRC_clones` folder; each file will be appended with a trailing number (e.g., `state_01_01_1.mrc`, `state_01_01_2.mrc`, `state_01_01_3.mrc` if `state_01_01.mrc` was given an occupancy of 3 in the occupancy map).
