# README
## Required packages
- Chimera (UCSF)
- Python
- Anaconda with `synth` environment activated (see main repository README)

---

## Instructions for generating the first Conformational Motion (CM1)
- The `1_GenStates_CM1` folder contains the original Hsp90 monomer arms (as extracted from PDB 2cg9), entitled `monoA.pdb` and `monoB.pdb`. If running a different protein, you will need to isolate your own subunits in a similar fashion based on your preferred structural motion for CM1.
- To remove undesirable overlap of atoms during CM1, as a convenience only, a few residues were first removed from each of these monomers. The resulting files are entitled `monoA_snip.pdb` and `monoB_snip.pdb`.
- The script `Gen_CM1.py` will automatically read in these structures and apply a set of discrete transformations on them, resulting in *N* CM1 states. Before running this script from the command line interface (from within this same directory), you will need to alter the following variables depending on your needs:
-- `monoA`: filename of the first subunit
-- `monoB`: filename of the second subunit
-- `range(1,21)`: range of states to be generated (e.g., 20)
-- Chimera logic under the `range(1,21)` loop, to depict the motions of interest
- Running `Gen_CM1.py` will generate *N* CM1 states (`.pdb`) in the output folder `Generate_CC1`

---

### Remarks
- Both CM1 and CM2 could potentially be created in this way. However, in this exemplory workflow, CM2 was instead created using PyMOL (as a convenience for the desired motions). As such, either of these scripts can be used as inspiration for generating your CM1xCM2 state space, or an entirely different method altogether. Just make sure that the output `.pdb` files for this state space are organized in the proper folders before proceeding to subsequent steps.
