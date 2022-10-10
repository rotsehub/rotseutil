import numpy as np
import matplotlib.pyplot as plt
import os
from astropy.io import fits

directory = 'the/directory/you/want/to/use' #replace this with the location of the directory

for filename in os.listdir(directory):
    if filename.endswith("_c.fit"):    #loops through all _c.fit files
        hdulist = fits.open('*_c.fit') 
	output = '*_c.txt'
        hdu = hdulist[0]
        headername=hdu.header['EXPTIME'] #to just extract 'EXPTIME' header
        data = fits.getdata('*_c.fit', extname='EXPTIME') #to obtain data from the EXPTIME column
	np.savetxt(output, data, fmt='%d', delimiter=',') #saves the EXPTIME data to a new csv file
        continue
    else:
        print("Code failed, needs a fix")
        continue



