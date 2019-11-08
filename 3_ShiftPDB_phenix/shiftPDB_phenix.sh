# script to re-center all PDBs based on common center-of-mass coordinates

for i in ../2_GenStates_CC2/Generate_CC2/*.pdb
do
    out=`basename $i`
    outFile=/mnt/Data2/evanseitz/Hsp90_Online/3_ShiftPDB_phenix/PDB_shifts/$out
    echo "$outFile"
    phenix.pdbtools "${i}" output.file_name=$outFile sites.translate="115.5 58.1 -39.5"
done

