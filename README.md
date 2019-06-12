# rotseutil
Common tools for multiple ROTSE packages.

#+++++++++ M2 data management +++++++++++++++++++++++++++++++++++

#Running scripts/arrangedata 
====================================

# Example run from the current directory (add to PATH for production runs)

./data_manage_M2 /scratch/group/astro/data/ROTSE/rotse21/disk2/rotse3

For all the numeric directories under the given directories and for all the telescope types [3a,3b,3c,3d]
=> Copies files from the respective image and prod directories (coadds to separate direcotories) inside outpath given. 

outpath='/scratch/group/astro/data/ROTSE' #- default
outdir=$outpath'/rdata/'${tele}'/'$yy'/'$mm'/'$dd
logfile=$outpath'/rdata/'$ndate'_'$tele'_copylog.txt'

#- Assuming 140903 was inside the source directory

The target directory tree for this example will be
/scratch/group/astro/data/ROTSE/rdata/3b/14/09/03/image 
/scratch/group/astro/data/ROTSE/rdata/3b/14/09/03/prod 

For coadds
/scratch/group/astro/data/ROTSE/rdata/3b/14/09/03/coadd/image
/scratch/group/astro/data/ROTSE/rdata/3b/14/09/03/coadd/prod

A log file /scratch/group/astro/data/ROTSE/rdata/140903_3b_copylog.txt 
will be written giving the source file and the target directory.

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
