'''
Created on Jul 15, 2017

@author: arnon
'''

from rotseutil.findburst_utils.sixty import sixty


def get_sexa(value, with_sign=False):
    '''Translates deg to sexa

    Args:
        value: degree
        with_sign: add +/- prefix sign.

    Returns:
        Sexa
    '''
    val_sixty = sixty(value,)
    sign = ''
    if not with_sign:
        sign = '+' if value > 0 else '-'

    val_sixty = [abs(i) for i in val_sixty]
    vals = "{}{:02d}{:02d}{:06.3f}".format(sign, *val_sixty)
    return vals


def deg2sexa(rain, decin):
    ''' convers ra and dec degreese to sexa

    Args:
        rain, decin: in degreese

    Returns:
        ras, decs: sexa strings
    '''
    ras = get_sexa(rain/15.0, with_sign=True)
    decs = get_sexa(decin)

    return ras, decs


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

        Example result:

            ROTSE1 J113810.766+474206.980

    '''
    ras, decs = deg2sexa(rain, decin)

    startstr = 'ROTSE1' if tele is None else tele

    name = "%s J%s%s" % (startstr, ras, decs)
    return name


if __name__ == "__main__":
    for decin, rain in [(47.7019389925, 174.544859023), (49.5787561507, 164.636139522), (10.5787561507, 5.636139522), (-10.5787561507, -5.636139522), ]:
        print('allow negative:', make_rotse_name(rain, decin))
