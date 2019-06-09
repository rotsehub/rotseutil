'''
Created on Jul 25, 2017

@author: Daniel Sela, Arnon Sela
'''


def sixty(scalar, trailsign=False, ):
    '''
    ;+
    ; NAME:
    ;    SIXTY()
    ; PURPOSE:
    ;    Converts a decimal number to sexagesimal.
    ; EXPLANATION:
    ;    Reverse of the TEN() function.
    ;
    ; CALLING SEQUENCE:
    ;    X = SIXTY( SCALAR, [ /TrailSign ] )
    ;
    ; INPUTS:
    ;    SCALAR -- Decimal quantity.
    ; OUTPUTS:
    ;    Function value returned = real vector of three elements,
    ;    sexagesimal equivalent of input decimal quantity.    Double
    ;       precision if the input is double, otherwise floating point.
    ;    By default, a negative number is signified by making the first non-zero
    ;    element of the output vection negative, but this can be modified with
    ;       the /TrailSign keyword.
    ;
    ; OPTIONAL INPUT KEYWORD:
    ;      /TrailSign - By default, SIXTY() returns a negative sign in the first
    ;         nonzero element.   If /TrailSign is set, then SIXTY() will return
    ;         always return a negative sign in the first element, even if it is
    ;         zero
    ; PROCEDURE:
    ;    Mostly involves checking arguments and setting the sign.
    ;
    ; EXAMPLE:
    ;    If x = -0.345d then sixty(x) = [0.0, -20.0, 42.0]
    ;                      and sixty(x,True) = [-0.0, 20.0, 42.0]
    ;-

    Changes History:
        Added dd range limit - force positive value by complementing to dd_range
        prevent adding negative sign to value of 0
    '''
    if not isinstance(scalar, float):
        scalar = float(scalar)

    ss = abs(3600.0*scalar)
    mm = abs(60.0*scalar)
    dd = abs(scalar)

    result = [0, 0, 0]
    result[0] = int(dd)
    result[1] = int(mm-60.0*result[0])
    result[2] = ss-3600.0*result[0] - 60.0*result[1]

    if scalar < 0:
        if trailsign:
            result[0] = -result[0]
        else:
            if result[0] != 0:
                result[0] = -result[0]
            elif result[1] != 0:
                result[1] = -result[1]
            elif result[2] != 0:
                result[2] = -result[2]
    return result


if __name__ == '__main__':
    import unittest
    from astropy.coordinates import Angle
    from astropy import units as u

    class TestSixtyMethod(unittest.TestCase):
        def test_1(self):
            self.assertEqual(sixty(-0.5), [0, -30, 0.0])

        def test_2(self):
            self.assertEqual(sixty(0.5), [0, 30, 0.0])

        def test_3(self):
            self.assertEqual(sixty(10.49999), [10, 29, 59.96399999999994])

        def test_4(self):
            dms = Angle(-0.5, unit=u.deg).dms
            result = list(dms._asdict().values())
            self.assertEqual(result, [-0.0, -30.0, -0.0])

    unittest.main()
