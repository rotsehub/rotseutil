General optional arguments-
    --save or -s: True/False; saves script output to .dat file; optional; default is True
    --plot or -p: True/False; plots interactive figure from script output; optional; default is True
    --pickleplot or -pkl: True/False; saves interactive figure; optional; default is False
    --hjd: displays time in HJD on plots; optional; default is False    
    --verbose or -v: True/False; prints script output to terminal

mjd2hjd.py
    terminal> python mjd2hjd.py file rightAscension declination --epoch --truncateHjd True/False --verbose
    file: path to target's MJD light curve .dat file or path to match structure directory
    rightAscension: right ascension of target object
    declination: declination of target object
    --epoch or -e: Given the MJD epoch of an observation, prints HJD epoch of that specific observation to terminal; optional
    --truncateHjd or -t: subtract 2400000 from HJD, needed for single_phase; optional; default is False

mergelightcurves.py
    terminal> python mergelightcurves.py fileA fileB mergedFileName --verbose
    fileA: path to first light curve .dat file or match structure directory
    fileB: path to second light curve .dat file or match structure directory
    mergedFileName: name to save merged light curve under

lc.py
    terminal> python lc.py file rightAscension declination --save --plot --pickleplot --hjd --verbose
    file: path to target light curve .dat file or path to match structure directory
    rightAscension: right ascension of target object
    declination: declination of target object

phasedlc.py
    terminal> python phasedlc.py file rightAscension declination period --epoch --save --plot --plotlc --pickleplot --hjd --verbose
    file: path to target's light curve .dat file or path to match structure directory
    rightAscension: right ascension of target object
    declination: declination of target object
    period: period to phase light curve using
    --epoch or -e: Given the epoch of an observation, will use that observation as the zeropoint of the phased light curve; optional
    --plotlc or -plc: True/False; plot light curve alongside phased light curve; optional; default is False
