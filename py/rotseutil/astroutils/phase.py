def phaseLightCurve(lightCurve, period, epoch):
    from math import trunc
    from operator import itemgetter
    if epoch < 0:
        epoch = 0
    phasedLightCurve = [(x[0] - epoch) / period for x in lightCurve]
    phasedLightCurve = [x - trunc(x) + 1 if x < 0 else x - trunc(x) for x in phasedLightCurve]
    phasedLightCurve = [[phasedLightCurve[x], lightCurve[x][1], lightCurve[x][2]] for x in range(len(lightCurve))]
    for x in range(len(phasedLightCurve)):
        phasedLightCurve.append([phasedLightCurve[x][0] + 1, phasedLightCurve[x][1], phasedLightCurve[x][2]])
    phasedLightCurve.sort(key = itemgetter(0))
    return phasedLightCurve
