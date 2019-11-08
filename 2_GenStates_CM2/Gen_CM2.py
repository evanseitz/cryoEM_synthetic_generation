import os
from pymol import stored
from pymol import cmd

# INSTRUCTIONS: run via 'pymol Gen_CM2.py'; outputs will go into
    # Generate_CM2 folder

pyDir = os.getcwd() #python file location
parDir = os.path.abspath(os.path.join(pyDir, os.pardir))
CM1_dir = os.path.join(parDir,'1_GenStates_CM1/Generate_CM1')
outDir = os.path.join(pyDir, 'Generate_CM2')

CM1_paths = []
for root, dirs, files in os.walk(CM1_dir):
    for file in sorted(files):
        if not file.startswith('.'): #ignore hidden files
            if file.endswith(".pdb"):
                CM1_paths.append(os.path.join(root, file))

for CM in CM1_paths:
    cmd.load(CM)

idx = 1
for CM in CM1_paths:

    if idx < 10:
        CM_name = 'CM1_0%s' % idx
    else:
        CM_name = 'CM1_%s' % idx

    cmd.select('%s and resi 12-442 and chain B' % CM_name)
    
    for i in range(1,21):
        print(CM_name, i)
        cmd.rotate('z', 2, 'sele')

        # SAVE:
        if idx < 10 and i < 10:
            cmd.save('%s/state_0%s_0%s.pdb' % (outDir, idx, i), CM_name)
        elif idx < 10 and i >= 10:
            cmd.save('%s/state_0%s_%s.pdb' % (outDir, idx, i), CM_name)
        elif idx >= 10 and i < 10:
            cmd.save('%s/state_%s_0%s.pdb' % (outDir, idx, i), CM_name)
        else:
            cmd.save('%s/state_%s_%s.pdb' % (outDir, idx, i), CM_name)

    #cmd.delete(CM_name)
    idx += 1
        
