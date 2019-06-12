'''
Created on Jul 21, 2017

@author: arnon
'''

import numpy as np


def meanabsdev(vector, Double=None, Median=None, NaN=None):
    ''' MeanAbsDev computes the mean absolute deviation (average deviation)
    of an N-element vector.

    Args:
        vector: An N-element vector of type integer, float or double.
        Double: If set to a non-zero value, MEANABSDEV performs its
                computations in double precision arithmetic and returns
                a double precision result. If not set to a non-zero value,
                the computations and result depend upon the type of the
                input data (integer and float data return float results,
                while double data returns double results). This has no
                effect if the Median keyword is set.
        Median: If set to a non-zero value, meanabsdev will return
                the average deviation from the median, rather than
                the mean.  If Median is not set, meanabsdev will return
                the average deviation from the mean.
        NaN: If set, treat NaN data as missing.

    Returns:
        mean absolute deviation
    '''
    if Median is not None:
        if NaN is not None:
            whereNotNaN = np.where(np.isfinite(vector))
            whereNotNaN = whereNotNaN[0]
            nanCount = len(whereNotNaN)

            if nanCount > 0:
                middle = np.median(vector[whereNotNaN])
            else:
                middle = 0
                raise Exception("Trying to calculate Median but all items are NaN")
        else:
            middle = np.median(vector)
    else:
        middle = np.mean(vector,)

    return np.mean(np.abs(vector - middle))
