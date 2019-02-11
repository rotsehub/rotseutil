'''
Created on Jul 21, 2017

@author: Daniel Sela, Arnon Sela
'''

import numpy as np
from scipy import stats as scistats
from rotseutil.meanabsdev import meanabsdev


def lightcurve(mag, err, m_lim, thresh, errfact, var):
    '''
    ; Purpose:  Determine if have range of magnitudes consistent with search
    ;
    ; Adopted from idl procedure

    ; Find general lightcurve characteristics

    '''
    var.ngdobs = len(mag)
    iobs = np.argmax(mag)
    var.maxmag = max(mag)
    var.errmaxmag = err[iobs]
    var.minmag = min(mag)
    var.maxsig = max(-1.0*(mag - m_lim)/err)
    var.delta = var.maxmag - var.minmag
    var.avgdev = meanabsdev(mag)

    var.avgmag = np.mean(mag)
    var.sdev = np.sqrt(np.var(mag))
    var.skew = scistats.skew(mag)
    var.kurt = scistats.kurtosis(mag)
    var.mdnerr = np.median(err)
    var.avgdevsig = var.avgdev/var.mdnerr

    # Calculate most significant variation

    maxdelta = np.zeros(var.ngdobs, dtype=float)
    maxerr = np.zeros(var.ngdobs, dtype=float)
    err2 = err**2.0
    for l in range(var.ngdobs):
        diffs = np.abs(mag[l] - mag)
        sigs = diffs / np.sqrt(err2 + err2[l])
        i = np.where(np.logical_and.reduce((diffs > thresh, sigs > errfact, sigs > maxerr[l])))
        i = i[0]
        if len(i) > 0:
            iobs = np.argmax(sigs[i])
            maxerr[l] = sigs[i][iobs]
            maxdelta[l] = diffs[iobs]

    iobs = np.argmax(maxerr)
    var.bestsig = maxerr[iobs]
    var.bestdelta = maxdelta[iobs]

    # Calculate lightcurve chi-squared

    chisq = np.sum(((mag - var.avgmag)/err)**2.0)
    dof = float(var.ngdobs) - 1.0
    var.chisq = chisq / float(dof)
    iobs = np.argmax(np.abs(mag-var.avgmag))
    i = np.where(mag != mag[iobs])
    i = i[0]
    if len(i) > 2:
        var.sdevcl = np.var(mag[i])
        var.avgdevsigcl = meanabsdev(mag[i])/np.median(err[i])
        avgmag_clip = np.mean(mag[i])
        var.chisqcl = np.sum(((mag[i] - avgmag_clip)/err[i])**2.0)/(dof-1.0)
