Information about fieldfinder.py 

How to use?
For an object with RA and DEC coordinates known,

python fieldfinder.py --ra "given RA" --dec "given DEC"

This code outputs to a csv file a list of fields that cover the objects with given coordinates.

*This is a preliminary version of the code, and it currently takes 2-3 hours to go through entire ROTSE III-b data - from 2003-2015. Maybe disadvantageous to run on a login node in M3. More updates coming soon...


Information about DESI-ROTSEcoord.ipynb

This Jupyter notebook maps out the overlap in DESI and ROTSE fields.
Currently we are comparing the overlap with DESI EDR data - but will soon be replaced with the full projected 5 year DESI footprint.

