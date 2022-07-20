def makeLightCurvePlot(lightCurve, ax, hjd):
    ax.errorbar([x[0] for x in lightCurve], [x[1] for x in lightCurve], yerr = [x[2] for x in lightCurve], fmt='o', label = 'Light Curve')
    if hjd:
        if lightCurve[0][0] < 2400000:
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
    fig, ax = plt.subplots(1)
    ax = makeLightCurvePlot(lightCurve, ax, hjd)
    ax.set_title(f'Target: {rightAscension:.5f} {declination:.5f}\nObservations: {len(lightCurve)}')
    return fig, ax

if __name__ == "__main__":
    import argparse
    from openlightcurve import openLightCurve
    from convert2decicoords import convertCoords2Deci
    from pickleplot import makePickledPlot
    from matplotlib.pyplot import show
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = str, help = 'Path to target\'s light curve file')
    parser.add_argument('rightAscension', type = str, help = 'Target\'s right ascension')
    parser.add_argument('declination', type = str, help = 'Target\'s declination')
    parser.add_argument('--hjd', type = bool, choices = [True, False], default = False, help = 'Epochs are in HJD')
    parser.add_argument('--picklePlot', '-p', type = bool, choices = [True, False], default = False, help = 'Save interactive figure as a .pkl file')
    args = parser.parse_args()
    file = args.file
    rightAscension = args.rightAscension
    declination = args.declination
    picklePlot = args.picklePlot
    hjd = args.hjd
    lightCurve = openLightCurve(file)
    rightAscension, declination = convertCoords2Deci(rightAscension, declination)
    fig, ax = plotLightCurve(lightCurve, rightAscension, declination, hjd)
    if picklePlot:
        fileName = f'fig_ra{rightAscension:.5f}+dec{declination:.5f}'
        makePickledPlot(fig, f'fig_ra{rightAscension:.5f}+dec{declination:.5f}')
    show()
