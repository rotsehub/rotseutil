import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as pf
import sys
print (sys.argv)
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-d", "--datedir", help="subdirectory of the night")
argParser.add_argument("-r", "--ra", help="ra")
argParser.add_argument("-z", "--dec", help="dec")

args = argParser.parse_args()
print("args=%s" % args)

print("Night subdirectory=%s" % args.datedir)
print("ra=%s" % args.ra)
print("dec=%s" % args.dec)
#night = args.datedir.replace('/','')
#a = pf.open('/work/group/astro/rotse/data/'+args.telescope+'/'+ args.datedir +'/prod/'+ str(night) +'_'+ args.field +'_'+ args.telescope +''+ args.image +'_cobj.fit')
import os
import re
import pandas as pd
df = pd.DataFrame(columns=['Month','Date','Field'])
dict_list = []
fields=[]
fieldfind = []
uf = []
# assign directory
for yr in range(3,16,1):
    print("Year :",yr)
    for mon in range(1,13,1):
        print("Month : ",mon)

        for date in range(1,32,1):
            print("We are on day ",date)
        #date = 5
            directory = '/work/group/astro/rotse/data/3b/{0:02}/{1:02}/{2:02}/prod/' .format(yr,mon,date)
            if (os.path.exists(directory)):
                for filename in os.listdir(directory):
                    f = os.path.join(directory, filename)
                #print(f)
                    if (os.path.exists(f)):
                 #   print(f)
                
                        if (f.endswith("cobj.fit")):
                            #print(filename)
                            try:
                                found = re.search('_(.+?)_3b',f).group(1)
                                
                        #fields.append(found)
                            except AttributeError:
                                found = "No match"
                            #print(found)
                            fields.append(found)
                    #print(fields)
                        else:
                            continue
                    else:
                        continue
            
                ufields = list(set(fields))
                #print("List of unique fields =",ufields)
                for u in ufields:
                    #print("------------------FIELD NAME -------------- :",u)
                            #print("Field:",ufields)
                    for num in range(1,200,1):
                            #a = pf.open(directory+'130905_'+u+'_3b{0:03}_cobj.fit'.format(num))
                        ad = directory+'{0:02}{1:02}{2:02}_'.format(yr,mon,date)+u+'_3b{0:03}_cobj.fit'.format(num)
                        if (os.path.exists(ad)):#FileNotFoundErrore
                            #print("path exists")
                            break 
                                #aa = ad#continue #a = pf.open(ad)#break #print("Path exists")
                        else:
                            pass #continue    
                
                    try:
                        a = pf.open(ad)
                    except OSError as e:
                        print("unable to open")
                        #return
                    ahead = a[0].header
                    mra = ahead['MOUNTRA']
                    mdec = ahead['MOUNTDEC']
                    #print('Mount RA =',mra)
                    #print('Mount DEC =',mdec)
                    fov = 1.85 #rotse FOV = 1.85x1.85 deg
                    ra_l = mra - (fov/2)/np.cos(mdec*(np.pi)/180)
                    ra_h = mra + (fov/2)/np.cos(mdec*(np.pi)/180)
                    mdecl = mdec - fov/2
                    mdech= mdec + fov/2
                    ra_ll = mra - (fov/2)/np.cos(mdecl*(np.pi)/180)
                    ra_lh = mra + (fov/2)/np.cos(mdecl*(np.pi)/180)
                    ra_hl = mra - (fov/2)/np.cos(mdech*(np.pi)/180)
                    ra_hh = mra + (fov/2)/np.cos(mdech*(np.pi)/180)
                    """print(np.cos(mdec*(np.pi)/180))
                                    print("RA lower limit (corrected) at field centre:",ra_l)
                                    print("RA upper limit (corrected) at field centre: ",ra_h)
                                    print("RA lower limit (corrected) at dec low:",ra_ll)
                                    print("RA upper limit (corrected) at dec low: ",ra_lh)
                                    print("RA lower limit (corrected) at dec high:",ra_hl)
                                    print("RA upper limit (corrected) at dec high: ",ra_hh)

                                    print("trapezoid coordinates:")
                                    print("bottom-left:",ra_ll,",",mdecl)
                                    print("bottom-right:",ra_lh,",",mdecl)
                                    print("top-left:",ra_hl,",",mdech)
                                    print("top-right:",ra_hh,",",mdech)
                    """
                    #del fields           
                    if (((float(args.dec) > mdecl) and (float(args.dec) < mdech)) and ((float(args.ra) > ra_ll) and (float(args.ra) < ra_hh))):
                        #print("OBJECT EXISTS IN THIS FIELD!!!")
                        fieldfind.append(u)
                        uf = list(set(fieldfind))
                            
                    #else:
                        #print("Object  Not Found. :(")
                    #    break
                    #print("Object with given RA and DEC values found in the following fields for date 13/09/"+str(date)+":",fieldfind)
                    fields.clear()
                 
            print("Object with given RA and DEC values found in the following fields for date "+str(yr)+"/"+str(mon)+"/"+str(date)+":",uf)#fieldfind)
            row_dict = {'Year':yr,'Month':mon,'Date':date,'Field':uf}#fieldfind}
            dict_list.append(row_dict)

df = pd.DataFrame.from_dict(dict_list)
df.to_csv('2003-2015fieldfinder_RA'+args.ra+'_DEC'+args.dec+'.csv')
        
        #ufields.clear()
            #print("Object with given RA and DEC values found in the following fields for date 13/09/"+str(date)+":",fieldfind)

                #delta_ra = (ra_h - ra_l)*np.cos(mdec)

                #delta_dec = fov
                #area = delta_ra*delta_dec
                #print("Field area =", area)
