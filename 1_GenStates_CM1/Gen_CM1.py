import os
from chimera import runCommand as rc

# INSTRUCTIONS: run this file from same directory as mono_A_snip.pdb,
    # and mono_B_snip.pdb are located... CC1 states will output to
    # Generate_CC1 folder

pyDir = os.path.dirname(os.path.abspath(__file__)) #python file location
parDir = os.path.abspath(os.path.join(pyDir, os.pardir))
outDir = os.path.join(pyDir, 'Generate_CM1')
monoA = os.path.join(pyDir, 'monoA_snip.pdb')
monoB = os.path.join(pyDir, 'monoB_snip.pdb')

rc('open' + monoB)
rc('open' + monoA)
rc('select :677.a') #select central hinge atom (LEU 674)

rot = 1
for i in range(1,21): #-20 degrees total
    if i == 1: #don't rotate for state 1
        rc('combine #0-1, name CM1_%s' % i)
        rc('write relative #0 format pdb #2 %s/CM1_0%s.pdb' % (outDir,i))
    else:
        rc('turn 0,1,0 %d center sel models #0' % rot)
        rc('combine #0-1, name CM1_%s' % i)
        if i < 10:
            rc('write relative #0 format pdb #2 %s/CM1_0%s.pdb' % (outDir,i))
        else:
            rc('write relative #0 format pdb #2 %s/CM1_%s.pdb' % (outDir,i))
    rc('close #2')
