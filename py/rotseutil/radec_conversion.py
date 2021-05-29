"""
Convert RA and DEC to/from degree format

Hours to Degrees:
python radec.py -r 02:43:27.98 -d 37:20:44.7 -s

Degrees to Hours:
python radec.py -r 40.866583 -d 37.34575 -f
"""
import sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-s','--hour',default=False,action='store_true',dest='hour')
parser.add_argument('-f','--degree',default=False,action='store_true',dest='degree')
parser.add_argument('-r','--ra',type=str,required=True,dest='ra')
parser.add_argument('-d','--dec',type=str,required=True,dest='dec')
args=parser.parse_args()

if args.hour:
    ra_in = args.ra
    dec_in = args.dec
    ra = ra_in.split(':')
    dec = dec_in.split(':')

    ra_out = float(ra[0])*15. + float(ra[1])/4. + float(ra[2])/240.

    if float(dec[0]) >= 0.:
        dec_out = float(dec[0]) + float(dec[1])/60. + float(dec[2])/3600.
    else:
        dec_out = float(dec[0]) - float(dec[1])/60. - float(dec[2])/3600.

elif args.degree:
    ra_in = float(args.ra)
    dec_in = float(args.dec)

    ra_hr = int(ra_in/15.)
    ra_min = int((ra_in/15. - ra_hr)*60.)
    ra_sec = round((((ra_in/15. - ra_hr)*60.) - ra_min)*60.,2)
    ra_out = '{}:{}:{}'.format(ra_hr,ra_min,ra_sec)

    if dec_in >= 0.:
        dec_hr = int(dec_in)
        dec_min = int((dec_in - dec_hr)*60.)
        dec_sec = round((((dec_in - dec_hr)*60.) - dec_min)*60.,2)
    else:
        dec_hr = int(dec_in)
        dec_min = int((dec_in + dec_hr)*60.)
        dec_sec = round((((dec_in + dec_hr)*60.) + dec_min)*60.,2)
    dec_out = '{}:{}:{}'.format(dec_hr,dec_min,dec_sec)

else:
    print("Must provide coordinate format: hour or degree")
    sys.exit()

print('RA: {} -> {}'.format(ra_in,ra_out))
print('DEC: {} -> {}'.format(dec_in,dec_out))


