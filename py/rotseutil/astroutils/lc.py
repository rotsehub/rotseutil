import argparse
from evalboolarg import evalBoolArg
from readcurve import readCurve
from writecurve import saveLightCurve
from convert2decicoords import convertCoords2Deci
from plotCurve import plotLightCurve
from pickleplot import makePickledPlot
from matplotlib.pyplot import show

def main(file, rightAscension, declination, save, plot, picklePlot, verbose, hjd):
    rightAscension, declination = convertCoords2Deci(rightAscension, declination)
    lightCurve = readCurve(file, rightAscension, declination)
    if verbose:
        for x in lightCurve:
            print(*x)
    if save:
        saveLightCurve(lightCurve, f'lightcurve_ra{rightAscension:.5f}+dec{declination:.5f}.dat')
    if plot or picklePlot:
        fig, ax = plotLightCurve(lightCurve, rightAscension, declination, hjd)
        if picklePlot:
            makePickledPlot(fig, f'fig_ra{rightAscension:.5f}+dec{declination:.5f}')
        else:
            show()

parser = argparse.ArgumentParser()
parser.add_argument('file', type = str, help = 'Path to target\'s light curve file')
parser.add_argument('rightAscension', type = str, help = 'Target\'s right ascension')
parser.add_argument('declination', type = str, help = 'Target\'s declination')
parser.add_argument('--save', '-s', type = str, default = True, help = 'Save light curve to .dat file')
parser.add_argument('--plot', '-p',type = str, default = True, help = 'Show interactive light curve plot')
parser.add_argument('--picklePlot', '-pkl', type = str, default = False, help = 'Save interactive figure as a .pkl file')
parser.add_argument('--hjd', type = str, default = False, help = 'Epochs are in HJD')
parser.add_argument('--verbose', '-v', type = str, default = False, help = 'Print light curve to terminal')
args = parser.parse_args()
file = args.file
rightAscension = args.rightAscension
declination = args.declination
save = evalBoolArg(args.save, True)
plot = evalBoolArg(args.plot, True)
picklePlot = evalBoolArg(args.picklePlot, False)
verbose = evalBoolArg(args.verbose, False)
hjd = evalBoolArg(args.hjd, False)
main(file, rightAscension, declination, save, plot, picklePlot, verbose, hjd)
