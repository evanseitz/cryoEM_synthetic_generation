# README
## Required packages
- Python
- Anaconda with `synth` environment activated (see main repository README)

---

## Instructions for aligning all structures
- The `5_GenOcc_python` folder contains the exemplary `Occ2D_1k.py` and `Occ2D_5k.py` scripts, which can be used to generate customized occupancy maps (with 1000 and 5000 total occupancies per state space, respectively). Before running either script (e.g., via `python Occ2D_1k.py`) from the command line interface (from within this same directory), you will need to alter the following depending on your needs:
  - `def f1(x, y)`: specific function for generating the occupancy map, including discrete alterations to that map within the subsequent section (`if 1:`)
  - `range(0,20)`: each range in this double loop needs to be adjusted to match the number of states (*N*, *M*) chosen
- Running either `Occ2D_1k.py` or `Occ2D_5k.py` will generate a corresponding NumPy (`.npy`) data files. The name of this file will be needed in subsequent steps.

