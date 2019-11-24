# README
## Required packages
- Python
- Anaconda with `synth` environment activated (see main repository README)

---

## Instructions for aligning all structures
- The `7_GenSTARs_python` folder contains the `GenStars.py` script, which will generate a unique alignment file for each of your cloned Coulomb potential maps (`.mrc`) created in the previous step. Before running this script (via `python GenStars.py`) from the command line interface (from within this same directory), you will need to alter the following depending on your needs:
  - `S2`: change the file listed in this variable (default `proj812.txt` for 812 PDs) to switch between different tessellated spheres; several options have been provided, along with a Cinema4D script (`PDs.c4d`) for generating your own patterns. You may also want to rename the default number used in your `alignOut` file to match this choice
  - `quatsGaussian.op(S2)`: turn this variable on (`if 1:`) for applying quaternion transformations on each image about its original PD location on the S2 sphere. Inside of the `quatsGaussian.py` script, you may want to additionally change the angle used in the first quaternion transformation (`w1`) which corresponds to the spread of each image from its PD center
  - `df`: alter the range of defocus values to sample from for each image
  - `x,y`: alter the x and y shifts defining the object's center in each image
- Running `GenStars.py` will create all alignment files in the `STARs` folder, which are needed for subsequent projections. As well, once these alignment files are generated, running `python mayavi_viewer.py` provides a visualization tool for observing the final distribution of images on the S2 sphere.
