def saveLightCurve(lightCurve, fileName):
    lightCurve.sort()
    from numpy import savetxt
    print(f"You can find a copy of the light curve named {fileName} in the current working directory")
    savetxt(fileName, lightCurve, fmt = '%.11f')
    