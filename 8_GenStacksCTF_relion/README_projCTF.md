# README
## Required packages
- RELION

---

## Instructions for aligning all structures
- The `8_GenStacksCTF_relion` folder contains the `relion_projCTF.sh` bash script, which will take projections of all Coulomb potential maps (`.mrc`). Before running this script (via `sh relion_projCTF.sh`) from the command line interface (from within this same directory), you will need to alter the following depending on your needs:
  - `for i in`: change the path before `/6_GenClones_python/` to match your system
  - `angFile`: change the path before `/7_GenSTARs_python/` as well as the correct filename (default `proj812`) if this was renamed in the previous step
  - `outFile`: change the path before `/8_GenStacksCTF_relion/` to match your system
- Running `relion_projCTF.sh` will generate an updated alignment file (`.star`) and image stack (`.mrcs`) for each of the previously cloned Coulomb potential maps (`.mrc`); these files can be found in the `stacks` output folder.
