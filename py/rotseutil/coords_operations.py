'''
Created on Jul 30, 2017

@author: Daniel Sela, Arnon Sela
'''


def decim_2_vec(decim):
    if isinstance(decim, str):
        decim = float(decim)

    neg = decim < 0
    temp = abs(decim)
    dd = int(temp/10000.0)
    temp -= dd*10000.0
    mm = int(temp/100.0)
    ss = temp-mm*100.0
    if neg:
        if dd != 0:
            dd = -dd
        elif mm != 0:
            mm = -mm
        else:
            ss = -ss
    vector = [dd, mm, ss]
    return vector


def sec_2_decim(sec):
    dd = int(sec/3600.00)
    mm = int((sec-dd*3600.0)/60.0)
    ss = sec-dd*3600.0-mm*60.0
    return ss+mm*100+dd*10000


def decim_2_sec(decim):
    neg = 1.0 if decim >= 0 else -1.0
    vec = decim_2_vec(abs(decim))
    result = sum([i*f for i, f in zip(vec, [3600.0, 60.0, 1.0])])
    return result*neg


def add_coords(coords, delta):
    ''' Adds (or substructs) number to (from) coords

    Args:
        coords: 235959.456 style coords
        delta: ss number to add (negative to sub)
    '''
    temp = decim_2_sec(coords)
    temp += delta
    return sec_2_decim(temp)


if __name__ == '__main__':
    print('sec_2_decim:')
    print('  ', sec_2_decim(59))
    print('  ', sec_2_decim(61.6))
    print('  ', sec_2_decim(14631))

    print('decim_2_sec:')
    print('  ', decim_2_sec(59.0))
    print('  ', decim_2_sec(101.6))
    print('  ', decim_2_sec(40351.0))
    print('  ', decim_2_sec(-000123.282))
    print('  ', decim_2_sec(000123.282))
    print('  ', decim_2_sec(000001.282))
    print('  ', decim_2_sec(231806.584))

    print('add_coords:')
    print('  ', add_coords(240036.98, 5))
    print('  ', add_coords(-010236.98, 500))
    print('  ', add_coords(010236.98, 500))
    print('  ', add_coords(230036.98, 5000))
