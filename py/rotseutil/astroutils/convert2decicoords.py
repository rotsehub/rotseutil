def convertCoords2Deci(rightAscension, declination):
    if rightAscension[6] == '.':
        rightAscension = float(''.join(rightAscension[:2])) * 15 + float(''.join(rightAscension[2:4])) * 0.25 + float(''.join(rightAscension[4:])) / 240
        declination = float(''.join(declination[:2])) + float(''.join(declination[2:4])) / 60 + float(''.join(declination[4:])) / 3600
    else:
        rightAscension = float(rightAscension)
        declination = float(declination)
    return rightAscension, declination

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('rightAscension', help = 'HoursMinutesSeconds.Seconds right ascension (remove J)')
    parser.add_argument('declination', help = 'DegreesArcMinutesArcSeconds.ArcSeconds declination (remove +)')
    args = parser.parse_args()
    rightAscension = args.rightAscension
    declination = args.declination
    deciRightAscension, deciDeclination = convertCoords2Deci(rightAscension, declination)
    print(f"Decimal Right Ascension: {deciRightAscension:.5f}\nDecimal Declination: {deciDeclination:.5f}")
