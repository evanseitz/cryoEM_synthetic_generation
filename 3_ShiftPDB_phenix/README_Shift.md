# README
## Required packages
- Phenix (Python-based Hierarchical ENvironment for Integrated Xtallography)

---

## Instructions for aligning all structures
- The `3_ShiftPDB_phenix` folder contains the `shiftPDB_phenix.sh` bash script, which will align all structures (`.pdb`) in the *N*x*M* state space to a common reference point. Before running this script (via `sh shiftPDB_phenix.sh`) from the command line interface (from within this same directory), you will need to alter the following depending on your needs:
  - `outFile`: the output location; only change the initial path to match your system (i.e., nothing past `/3_ShiftPDB_phenix/`)
  - `sites.translate`: replace these coordinates with the CoM of a given state (e.g., your `state_01_01.pdb`)
- Running `shiftPDB_phenix.sh` will generate *N*x*M* shifted structures (`.pdb`) in the output folder `PDB_shifts`
