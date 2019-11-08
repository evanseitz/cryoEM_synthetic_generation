for i in /mnt/Data2/evanseitz/Hsp90_Online/6_GenClones_python/MRC_clones/*.mrc
do
    out=`basename $i`
    angFile=/mnt/Data2/evanseitz/Hsp90_Online/7_GenSTARs_python/STARs/proj812_${out%.*}.star
    outFile=/mnt/Data2/evanseitz/Hsp90_Online/8_GenStacksCTF_relion/stacks/${out%.*}
    echo $outFile
    relion_project --i "${i}" --o $outFile --ang $angFile --ctf true
done
