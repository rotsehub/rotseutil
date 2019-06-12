'''
Created on Jul 15, 2017

@author: arnon
'''

from astropy.coordinates import Angle
from astropy import units as u


def get_sexa(value, with_sign=False):
    va = Angle(value, u.deg).signed_dms
    vals = "{:02d}{:02d}{:06.3f}".format(int(va.d), int(va.m), va.s)
    if with_sign:
        sign = '+' if va.sign > 0 else '-'
        vals = sign+vals
    return vals


def make_rotse_name(rain, decin, tele='ROTSE1'):
    '''
    ; Purpose:    To construct IAU sanctioned name for a source at the input
    ;    coordinates.
    ;
    ; Inputs:
    ;    rain = input RA
    ;    decin = input declination
    ;
    ; Return Value:  string containing name of source
    ;
    ; Adopted from make_rotse_name.pro
    ; Created: Daniel Sela, Arnon Sela

    create rotse name.

        Example of input data:

        DEC 47.7019389925
        RA 174.544859023

        DEC 49.5787561507
        RA 164.636139522

        DEC 49.0189291939
        RA 165.237955608

    '''
    ra = get_sexa(rain/15,)
    dec = get_sexa(decin, with_sign=True)

    startstr = 'ROTSE1' if tele is None else tele

    name = startstr + ' J' + ra + dec
    return name


if __name__ == "__main__":
    for decin, rain in [(47.7019389925, 174.544859023), (49.5787561507, 164.636139522), (10.5787561507, 5.636139522), (-10.5787561507, -5.636139522)]:
        print(make_rotse_name(rain, decin))
