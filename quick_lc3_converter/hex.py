import re

def hex2Bin(hexString):
    binNumber =  bin(int(hexString, 16))
    print(binNumber[2:]) # cut off the '0b' of the string

def hexCheck(hexString):
    #'^' and '$' match the string exactly
    pattern1 = re.compile("^0[x][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$")
    pattern2 = re.compile("^[x][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$")
    case1 = bool(re.search(pattern1, hexString))
    case2 = bool(re.search(pattern2, hexString))
    if case1:
        return 1
    elif case2:
        return 2
    else:
        return 3

def brain():
    hexString = "0xffff"
    checking = hexCheck(hexString)
    if checking == 2:
        hexString = '0' + hexString
        hex2Bin(hexString)
    elif checking == 1:
        hex2Bin(hexString)
    else:
        print("An error had occured. The input given does not specify the required format.")
brain()
