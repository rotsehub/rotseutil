#module load ds9/default
#module load SExtractor/2.19.5/gcc-4.9.1
#module load python/2.7.10
#module load anaconda/4.3.0/2

alias ldlib="export LD_LIBRARY_PATH=/grid/software/rotsesoftware/links"

export IDL_PATH=/grid/software/rotsesoftware/rsi/idl_5.5/lib:/grid/software/rotsesoftware/idl.lib/spline/test:+/grid/software/rotsesoftware/products/idlastron_v5.3:+/grid/software/rotsesoftware/products/idltools:+/grid/software/rotsesoftware/idl.lib:

export LD_LIBRARY_PATH=/grid/software/rotsesoftware/links
export EXTRACT_PAR=/grid/software/rotsesoftware/products/idltools/umrotse_idl/tools/sex/
export EXTRACT_CONFIG=/grid/software/rotsesoftware/products/idltools/umrotse_idl/tools/sex/
export EXTRACT_BIN=/grid/software/rotsesoftware/products/sextractor2.2.2/source
export PATH=/grid/software/rotsesoftware/idl.lib/spline/tools/:/grid/software/rotsesoftware/ImageDiff/bin:$PATH

#- to log into one of the idl nodes in maneframe
#alias idlnode="srun -n1 -p idl --pty $SHELL"
export IDL_STARTUP=/grid/software/rotsesoftware/rotse_environ/.idl.startup
export ZDBASE=/grid/software/rotsesoftware/products/database
export UA2_PATH=/grid/software/rotsesoftware/products/usno
export PYTHONPATH=/grid/software/rotsesoftware/ImageDiff/py:/grid/software/rotsesoftware/pythontools/empca:$PYTHONPATH

