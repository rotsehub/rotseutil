import argparse
from evalboolarg import evalBoolArg
from readcurve import readCurve
from writecurve import saveLightCurve
from convert2decicoords import convertCoords2Deci
from phase import phaseLightCurve
from plotCurve import plotPhaseCurve
from pickleplot import makePickledPlot
from matplotlib.pyplot import show

def main(file, rightAscension, declination, period, epoch, save, plot, plotlc, picklePlot, hjd, verbose):
    rightAscension, declination = convertCoords2Deci(rightAscension, declination)
    lightCurve = readCurve(file, rightAscension, declination)
    phasedLightCurve = phaseLightCurve(lightCurve, period, epoch)
    if verbose:
        for x in phasedLightCurve:
            print(*x)
    if save:
        saveLightCurve(phasedLightCurve, f'phasedlightcurve_ra{rightAscension:.5f}+dec{declination:.5f}.dat')
    if plot or picklePlot:
        if plotlc:
            fig, ax = plotPhaseCurve(phasedLightCurve, lightCurve, rightAscension, declination, period, epoch, hjd)
        else:
            fig, ax = plotPhaseCurve(phasedLightCurve, None, rightAscension, declination, period, epoch, hjd)
        if picklePlot:
            makePickledPlot(fig, f'fig_ra{rightAscension:.5f}+dec{declination:.5f}')
        if plot:
            show() 



parser = argparse.ArgumentParser()
parser.add_argument('file', type = str, help = 'Path to target\'s phased light curve file')
parser.add_argument('rightAscension', type = str, help = 'Target\'s right ascension')
parser.add_argument('declination', type = str, help = 'Target\'s declination')    
parser.add_argument('period', type = float, help = 'Period to phase light curve using')
parser.add_argument('--epoch', '-e', type = float, default = 0, help = 'Epoch to use as zeropoint (optional)')
parser.add_argument('--save', '-s', type = str, default = True, help = 'Save phased light curve to .dat file')
parser.add_argument('--plot', '-p', type = str, default = True, help = 'Show interactive phased light curve plot')
parser.add_argument('--plotlc', '-plc', type = str, default = False, help = 'Plot target\'s light curve')
parser.add_argument('--picklePlot', '-pkl', type = str, default = False, help = 'Save interactive figure as a .pkl file')
parser.add_argument('--hjd', type = str, default = False, help = 'Epochs are in HJD')
parser.add_argument('--verbose', '-v', type = str, default = False, help = 'Print light curve to terminal')
args = parser.parse_args()
file = args.file
rightAscension = args.rightAscension
declination = args.declination
period = args.period
epoch = args.epoch
save = evalBoolArg(args.save, True)
plot = evalBoolArg(args.plot, True)
plotlc = evalBoolArg(args.plotlc, False)
picklePlot = evalBoolArg(args.picklePlot, False)
hjd = evalBoolArg(args.hjd, False)
verbose = evalBoolArg(args.verbose, False)
main(file, rightAscension, declination, period, epoch, save, plot, plotlc, picklePlot, hjd, verbose)
