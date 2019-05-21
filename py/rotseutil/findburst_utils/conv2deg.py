'''
Created on Jul 21, 2017

@author: Daniel Sela, Arnon Sela
'''


def conv2deg(arcsec, pixscale=14.0):
    '''
    ;+
    ; NAME: conv2deg
    ;
    ; CALLING SEQUENCE:     conv2deg,byteword
    ;
    ; INPUTS:   arcsec: byte variable which contains the arcseconds level delta
    ;            scaled to the plate scale.
                pixscale: default 14.0
    ;
    ; Return Value: value in degrees.
    ;
    ; Adopted to Python: Daniel Sela, Arnon Sela 7-21-2017
    ;******************************************************************************
    '''

    renorm = 2.0*pixscale/255.0
    val = renorm*float(arcsec) - pixscale
    val = val/3600.0

    return val


if __name__ == '__main__':
    import numpy as np

    data = np.arange(9).reshape((9,))

    c = np.vectorize(conv2deg,)
    print(c(data))
