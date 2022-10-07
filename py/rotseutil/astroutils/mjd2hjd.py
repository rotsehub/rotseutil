def mjd2hjd(lightCurve, rightAscension, declination, epoch, truncateHjd):
    from math import radians, sin, cos
    from convert2decicoords import convertCoords2Deci
    rightAscension, declination = convertCoords2Deci(rightAscension, declination)
    rightAscension = radians(rightAscension)
    declination = radians(declination)
    jd = [x[0] + 2400000.5 for x in lightCurve]
    days = [x - 2451545 for x in jd]
    meanLongitude = [(0.9856474 * x + 280.46646) % 360 for x in days]
    meanAnomaly = [0.9856003 * x + 357.528 for x in days]
    trueLongitude = [meanLongitude[x] + 1.915 * sin(radians(meanAnomaly[x])) + 0.02 * sin(radians(2 * meanAnomaly[x])) for x in range(len(lightCurve))]
    radVector = [1.00014 - 0.01671 * cos(radians(x)) - 0.00014 * cos(radians(2 * x)) for x in meanAnomaly]
    meanObliqueEcliptic = [23.439 - 0.0000004 * x for x in days]
    hjdCorrection = [(8.3167 * radVector[x]) * ((cos(radians(trueLongitude[x])) * cos(rightAscension) * cos(declination) + (sin(radians(trueLongitude[x])) * (sin(radians(meanObliqueEcliptic[x])) * sin(declination) + cos(declination) * cos(radians(meanObliqueEcliptic[x])) * sin(rightAscension))))) * 0.000694444 for x in range(len(lightCurve))]
    if truncateHjd:
        hjd = [jd[x] - hjdCorrection[x] - 2400000 for x in range(len(lightCurve))]
    else:
        hjd = [jd[x] - hjdCorrection[x] for x in range(len(lightCurve))]
    HjdLightCurve = [[hjd[x], lightCurve[x][1], lightCurve[x][2]] for x in range(len(lightCurve))]
    if epoch != 0:
        epochIndex = [x for x in range(len(lightCurve)) if lightCurve[x][0] == epoch]
        epochIndex = epochIndex[0]
        epoch = hjd[epochIndex]
    return HjdLightCurve, epoch

if __name__ == "__main__":
    import argparse
    from evalboolarg import evalBoolArg
    from readcurve import readCurve
    from writecurve import saveLightCurve
    from convert2decicoords import convertCoords2Deci
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = str, help = 'Path to target\'s light curve file')
    parser.add_argument('rightAscension', type = str, help = 'Target\'s right ascension')
    parser.add_argument('declination', type = str, help = 'Target\'s declination')
    parser.add_argument('--epoch', '-e', type = float, default = 0, help = 'Extract specific epoch converted to HJD')
    parser.add_argument('--truncateHjd', '-t', type = str, default = False, help = 'Truncate HJD to HJD-2400000')
    parser.add_argument('--verbose', '-v', type = str, default = False, help = 'Print HJD light curve to terminal')
    args = parser.parse_args()
    file = args.file
    rightAscension = args.rightAscension
    declination = args.declination
    epoch = args.epoch
    truncateHjd = evalBoolArg(args.truncateHjd)
    verbose = evalBoolArg(args.verbose)
    lightCurve = readCurve(file, rightAscension, declination)
    HjdLightCurve, HjdEpoch = mjd2hjd(lightCurve, rightAscension, declination, epoch, truncateHjd)
    if verbose:
        for x in HjdLightCurve:
            print(*x)
    if epoch != 0:
        print(f'HJD Epoch: {HjdEpoch}')
    deciRightAscension, deciDeclination = convertCoords2Deci(rightAscension, declination)
    saveLightCurve(HjdLightCurve, f'HJDlightcurve_ra{(deciRightAscension):.5f}_dec{(deciDeclination):.5f}.dat')
