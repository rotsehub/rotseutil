def openLightCurve(file):
    data = [x.split() for x in list(open(file).read().splitlines())]
    lightCurve = [[float(n) for n in x] for x in data]
    lightCurve.sort()
    return lightCurve
