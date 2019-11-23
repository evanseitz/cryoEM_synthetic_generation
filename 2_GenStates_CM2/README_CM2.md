# README
## Required packages
- PyMOL
- Python
- Anaconda with `synth` environment activated (see main repository README)

---

## Instructions for generating the second Conformational Motion (CM2) and corresponding state space
- The `2_GenStates_CM2` folder contains the script `Gen_CM2.py`, which will read in the *N* previously generated CM1 structures (`.pdb`) and apply a second set of discrete transformations on them, resulting in a *N*x*M* state space. Before running this script (via `python Gen_CM2.py`) from the command line interface (from within this same directory), you will need to alter the following variables depending on your needs:
  - `if idx < 10`: if you previously generated *N* > 99 CM1 states, follow the same pattern for proper indexing (leading zeros); this logic also follows for the section underneath the `# SAVE` comment
  - `cmd.select`: range of residues to alter for CM2
  - `range(1,21)`: range of states to be generated for CM2 (e.g., 20)
  - `cmd.rotate`: chosen axis of rotation (e.g., `z`) and the angular increment for discrete rotations (e.g., `2`)
- Running `Gen_CM1.py` will generate the *N*x*M* state space (`.pdb`) in the output folder `Generate_CC2`

---

### Remarks
- The outputs from this script pertain to all combinations of CM1 and CM2. This script will have to be edited if more than 2 degrees of freedom are requested.
