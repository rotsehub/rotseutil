def makeCurvePlot(curve, ax, hjd, title):
    ax.errorbar([x[0] for x in curve], [x[1] for x in curve], yerr = [x[2] for x in curve], fmt='o', label = title)
    if hjd:
        if curve[0][0] < 2400000:
            ax.set(xlabel = 'Time (HJD - 2400000)')
        else:
            ax.set(xlabel = 'Time (HJD)')
    else:
        ax.set(xlabel = 'Time (MJD)')
    ax.set(ylabel = 'Magnitude')
    ax.invert_yaxis()
    ax.grid(axis = 'both', alpha = 0.75)
    ax.legend()
    return ax

def plotLightCurve(lightCurve, rightAscension, declination, hjd):
    import matplotlib.pyplot as plt
    from plotCurve import makeCurvePlot
    fig, ax = plt.subplots(1)
    ax = makeCurvePlot(lightCurve, ax, hjd, 'Light Curve')
    ax.set_title(f'Target: {rightAscension:.5f} {declination:.5f}\nObservations: {len(lightCurve)}')
    return fig, ax

def plotPhaseCurve(phasedLightCurve, lightCurve, rightAscension, declination, period, epoch, hjd):
    import matplotlib.pyplot as plt
    from plotCurve import makeCurvePlot
    if lightCurve != None:
        fig, ax = plt.subplots(2, sharey = True)
        ax1, ax2 = ax
        ax1 = makeCurvePlot(lightCurve, ax1, hjd, 'Light Curve')
        ax1.set_title(f'Target: {rightAscension:.5f} {declination:.5f} \n Observations: {len(phasedLightCurve)} Period: {period} Epoch: {epoch}')
        ax2 = makeCurvePlot(phasedLightCurve, ax2, hjd, 'Phased Light Curve')
    else:
        fig, ax = plt.subplots(1)
        ax.set_title(f'Target: {rightAscension:.5f} {declination:.5f} \n Observations: {len(phasedLightCurve)} Period: {period} Epoch: {epoch}')
        ax = makeCurvePlot(phasedLightCurve, ax, hjd, 'Phased Light Curve')
    return fig, ax
