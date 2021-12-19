# script to convert all re-centered PDBs into MRCs (`_1.mrc` represents the 1st copy of each)

for i in ../3_ShiftPDB_phenix/PDB_shifts/*.pdb
do
    out=`basename ${i%.*}_1.mrc`
    outFile=/mnt/Data2/evanseitz/Hsp90_Online/4_GenMRC_eman/MRCs/$out
    echo "$outFile"
    e2pdb2mrc.py "${i}" $outFile -A 1 -R 3 -B 320 #pixel size, resolution, box size (box size was originally 250)
done
