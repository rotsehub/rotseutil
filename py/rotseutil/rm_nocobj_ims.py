"""
Remove images where cobj doesn't exist for easier coaddition
"""
import os
import numpy as np

ls_image=sorted(os.listdir('./image'))
ls_prod=sorted(os.listdir('./prod'))

# list all dates of images
dates=[]
for f in range(len(ls_image)):
    dates.append(ls_image[f][0:6]) # indices 0:6 -> date string
dates=sorted(list(set(dates)))

# sort image and prod directories by night
ifiles=[]
pfiles=[]
for date in dates:
    inights=[]
    for i in range(len(ls_image)):
        if ls_image[i][0:6]==date:
            inights.append(ls_image[i])
    ifiles.append(inights)
    pnights=[]
    for p in range(len(ls_prod)):
        if ls_prod[p][0:6]==date:
            pnights.append(ls_prod[p])
    pfiles.append(pnights)

# remove exposures where corresponding cobj files don't exist
for n in range(len(ifiles)):
    if len(ifiles[n])!=len(pfiles[n]):
        iexp=[]
        for j in range(len(ifiles[n])):
            iexp.append(ifiles[n][j][22:25]) # indices 22:25 -> exposure id string
        pexp=[]
        for k in range(len(pfiles[n])):
            pexp.append(pfiles[n][k][22:25])
        for l in range(len(iexp)):
            if iexp[l] not in pexp:
                for m in range(len(ifiles[n])):
                    if ifiles[n][m][22:25]==iexp[l]:
                        print('No cobj file for image {}... Removing this file.'.format(ifiles[n][m]))
                        os.remove('./image/{}'.format(ifiles[n][m]))


