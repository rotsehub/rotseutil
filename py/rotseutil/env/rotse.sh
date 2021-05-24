module load ds9
module load idl/8.0
module load sextractor
module load python/2
#module load gcc-6.3
module load elementary-supernova
module load snid
module load singularity
#module load anaconda/4.3.0/2

alias sing="singularity shell --bind /scratch /hpc/applications/rotsesoftware/rotsesoftware.simg"

export IDL_PATH=/scratch/group/astro/sw/ROTSE/rotsesoftware/idl.lib/spline/tools:+/scratch/group/astro/sw/ROTSE/rotsesoftware/rsi/idl_5.5/lib:+/scratch/group/astro/sw/ROTSE/rotsesoftware/idl.lib/spline/test:+/scratch/group/astro/sw/ROTSE/rotsesoftware/products/idlastron_v5.3:+/scratch/group/astro/sw/ROTSE/rotsesoftware/products/idltools:+/scratch/group/astro/sw/ROTSE/rotsesoftware/idl.lib:+/scratch/group/astro/sw/ROTSE/rotsesoftware/rsi/idl/lib:+/scratch/group/astro/sw/ROTSE/rotsesoftware/idl.lib/gd_lib/idl81/lib:

export LD_LIBRARY_PATH=/scratch/group/astro/sw/ROTSE/rotsesoftware/links
export EXTRACT_PAR=/scratch/group/astro/sw/ROTSE/rotsesoftware/products/idltools/umrotse_idl/tools/sex/
export EXTRACT_CONFIG=/scratch/group/astro/sw/ROTSE/rotsesoftware/products/idltools/umrotse_idl/tools/sex/
export EXTRACT_BIN=/scratch/group/astro/sw/ROTSE/rotsesoftware/products/sextractor2.2.2/source
export PATH=/scratch/group/astro/sw/ROTSE/rotsesoftware/idl.lib/spline/tools/:/scratch/group/astro/sw/ROTSE/rotsesoftware/ImageDiff/bin:/users/rstaten/rotse/iraf:$PATH
export PATH=$HOME:$PATH

export IDL_STARTUP=/scratch/group/astro/sw/ROTSE/rotsesoftware/rotse_environ/.idl.startup
export ZDBASE=/scratch/group/astro/sw/ROTSE/rotsesoftware/products/database
export UA2_PATH=/scratch/group/astro/sw/ROTSE/rotsesoftware/products/usno
export PYTHONPATH=/scratch/group/astro/sw/ROTSE/rotsesoftware/pythontools/photutils:/scratch/group/astro/sw/ROTSE/rotsesoftware/ImageDiff/py:/grid/software/rotsesoftware/pythontools/empca:$PYTHONPATH

