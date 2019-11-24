# README
## Required packages
- Python
- Anaconda with `synth` environment activated (see main repository README)

---

## Instructions for aligning all structures
- The `9_GenSNR_pyRelion` folder contains the `GenStackAlign_All.py` script which can be used to generate the final image stack (`.mrcs`) and alignment file (`.star`) for your customized synthetic continuum dataset. The `GenStackAlign_5PD.py` is an exemplory script for creating smaller stacks (for testing or preview purposes). Before running one of these scripts (e.g., via `python GenStackAlign_All.py`) from the command line interface (from within this same directory), you will need to alter the following depending on your needs:
  - `stackOut, alignOut`: you may want to change the final output names of your image stack and alignment file; if so, this change must also be reflected in the line: `alignFile.write(...@___.mrc)`
  - `occFile`: the filename of the occupancy map used in previous steps
  - `noise_var`: altering the denominator of this fraction (default `0.1`) will change the SNR of each image
