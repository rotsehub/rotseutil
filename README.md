# rotseutil
Common tools for multiple ROTSE packages.

#+++++++++ M2 data management +++++++++++++++++++++++++++++++++++

#Running scripts/arrangedata 
====================================

# Example run from the current directory (add to PATH for production runs)

./data_manage_M2 /scratch/group/astro/data/ROTSE/rotse21/disk2/rotse3 140903 3b

Copies files to image and prod directories (coadds to separate direcotories) inside outpath. 

outpath='/scratch/group/astro/data/ROTSE'
outdir=$outpath'/rotse/'${tele}'/'$yy'/'$mm'/'$dd
logfile=$outpath'/rotse/'$ndate'_'$tele'_copylog.txt'

The directory tree for this example will be
/scratch/group/astro/data/ROTSE/rotse/3b/14/09/03/image
/scratch/group/astro/data/ROTSE/rotse/3b/14/09/03/prod

For coadds
/scratch/group/astro/data/ROTSE/rotse/3b/14/09/03/coadd/image
/scratch/group/astro/data/ROTSE/rotse/3b/14/09/03/coadd/prod

A log file /scratch/group/astro/data/ROTSE/rotse/140903_3b_copylog.txt 
will be written giving the source file and the target directory.

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
