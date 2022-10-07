def mergeLightCurves(fileA, fileB):
    from readcurve import openLightCurve
    mergedLightCurve = openLightCurve(fileA) + openLightCurve(fileB)
    mergedLightCurve.sort()
    return mergedLightCurve

if __name__ == "__main__":
    import argparse
    from evalboolarg import evalBoolArg
    from writecurve import saveLightCurve
    parser = argparse.ArgumentParser()
    parser.add_argument('fileA', help = 'Path to data file for light curve A')
    parser.add_argument('fileB', help = 'Path to data file for light curve B')
    parser.add_argument('mergedFileName', help = 'Title of merged light curve file')
    parser.add_argument('--verbose', '-v', type = bool, choices = [True, False], default = False, help = 'Print merged light curve to terminal')
    args = parser.parse_args()
    fileA = args.fileA
    fileB = args.fileB
    mergedFileName = args.mergedFileName
    verbose = evalBoolArg(args.verbose)
    mergedLightCurve = mergeLightCurves(fileA, fileB)
    if verbose:
        for x in mergedLightCurve:
            print(*x)
    saveLightCurve(mergedLightCurve, mergedFileName)
