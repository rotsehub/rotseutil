def openLightCurve(file):
    data = [x.split() for x in list(open(file).read().splitlines())]
    lightCurve = [[float(n) for n in x] for x in data]
    lightCurve.sort()
    return lightCurve

def openMatchStructures(file, rightAscension, declination):
    import os
    import glob
    from scipy.io import readsav
    from astropy.io import fits
    import numpy as np

    def readFitsFile(file, fitsIndex=1):
        try:
            hdus = fits.open(file, memmap = True)
            hdusExt = hdus[fitsIndex]
            match = hdusExt.data
        except Exception as e:
            raise Exception("cannot read fits data from file: %s" % (file,)) from e
        return match, 'ROTSE3'
    
    def readMatchFile(file, *args, **kwargs):
        try:
            match = readsav(file)['match']
        except Exception as e:
            raise Exception("cannot read match data from file: %s" % (file,)) from e
        return match, 'ROTSE1'
    
    def getDataFileRotse(file):
        if not os.path.isfile(file):
            raise Exception("file not found: %s" % (file,))  
        fileExt = file.rpartition('.')[2]
        if fileExt == 'fit':
            return 3
        else:
            return 1
    
    def readDataFile(file, fitsIndex=1, tmpDir='/tmp'):
        if not os.path.isfile(file):
            raise Exception("file not found: %s" % (file,))
        fileExt = file.rpartition('.')[2]
        if fileExt == 'fit':
            match, rotse = readFitsFile(file, fitsIndex)
        else:
            match, rotse = readMatchFile(file)
        return match, rotse
    
    def getMatchStructures(directory):
        cwd = os.getcwd()
        os.chdir(directory)
        matchStructures = list()
        fits = glob.glob("*match.fit")
        dats = glob.glob("*match.dat")
        datcs = glob.glob("*match.datc")
        for fit in fits:
            matchStructures.append(fit)
        for dat in dats:
            matchStructures.append(dat)
        for datc in datcs:
            matchStructures.append(datc)
        return matchStructures, cwd
    
    def findTarget(rightAscension, declination, matchStructures):
        filteredMatchStructures = list()
        targetLightCurve = list()
        for match in matchStructures:
            try:
                lightCurve = getData(rightAscension, declination, match)
                for x in lightCurve:
                    targetLightCurve.append(x)
                print(f"Target found in {match}")
                filteredMatchStructures.append(match)
            except IndexError:
                #print(f"Cannot find target in {match}; this match structure was removed from the list")
                pass
        return filteredMatchStructures, targetLightCurve
    
    def getData(rightAscension, declination, match):
        matchFile = None
        if isinstance(match, str):
            matchFile = match
            match, tele = readDataFile(matchFile)
        matchRa = match.field('RA')[0]
        matchDec = match.field('DEC')[0]
        cond = np.logical_and.reduce((np.abs(matchRa - rightAscension) < 0.001, np.abs(matchDec - declination) < 0.001))
        goodObj = np.where(cond)
        objid = goodObj[0]
        matchMagLim = match['STAT'][0]['M_LIM']
        matchExpTime = match.field('EXPTIME')[0]
        matchMagErr = match.field('MERR')[0][objid][0]
        matchMag = match.field('M')[0][objid][0]
        matchJd = match.field('JD')[0]
        data = [(matchJd[x], matchMag[x], matchMagErr[x], matchExpTime[x] / 86400, matchMagLim[x]) for x in range(len(matchJd)) if 0 < matchMag[x] < 99]
        return data
    
    matchStructures, cwd = getMatchStructures(file)
    matchs, lightCurve = findTarget(rightAscension, declination, matchStructures)
    lightCurve.sort()
    return lightCurve

def readCurve(file, rightAscension, declination):
    import os
    if os.path.isdir(file):
        curve = openMatchStructures(file, rightAscension, declination)
    else:
        curve = openLightCurve(file)
    return curve

if __name__ == "__main__":
    import argparse
    from evalboolarg import evalBoolArg
    from writecurve import saveLightCurve
    from convert2decicoords import convertCoords2Deci
    parser = argparse.ArgumentParser()
    parser.add_argument('matchDir', type = str, help = 'Path to match structure directory')
    parser.add_argument('rightAscension', type = str, help = 'Target\'s right ascension')
    parser.add_argument('declination', type = str, help = 'Target\'s declination')
    parser.add_argument('--truncateFields', '-t', type = str, default = False, help = 'Truncate observations\' fields to epoch, magnitude, and error')
    args = parser.parse_args()
    matchDir = args.matchDir
    rightAscension = args.rightAscension
    declination = args.declination
    truncateFields = evalBoolArg(args.truncateFields, False)
    rightAscension, declination = convertCoords2Deci(rightAscension, declination)
    lightCurve = openMatchStructures(matchDir, rightAscension, declination)
    fileName = f'extractedlightcurve_ra{(rightAscension):.5f}_dec{(declination):.5f}'
    saveLightCurve(lightCurve, fileName)
