# README
## Required packages
- Python
- Anaconda with `synth` environment activated (see main repository README)

---

## Instructions for generating occupancy maps
- The `5_GenOcc_python` folder contains exemplary occupancy generation scripts (e.g., `Occ2D_1k.py`), which can be used to generate customized occupancy maps (e.g., having 1000 total occupancy for `Occ2D_1k.py`). Before running one of these scripts (e.g., via `python Occ2D_1k.py`) from the command line interface (from within this same directory), you will need to alter the following depending on your needs:
  - `def f1(x, y)`: specific function for generating the occupancy map, including discrete alterations to that map within the subsequent section (`if 1:`)
  - `range(0,20)`: each range in this double loop needs to be adjusted to match the number of states (*N*, *M*) chosen
- Running `Occ2D_1k.py` (or `Occ2D_5k.py`, etc.) will generate a corresponding NumPy (`.npy`) data file; the name of this file will be needed in subsequent steps.

