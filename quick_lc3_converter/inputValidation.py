import re
"""
Author: Adam Nieto

"""
def pcCheck(pc):
    #'^' and '$' match the string exactly
    pattern = re.compile("^[0-1A-F][0-1A-F][0-1A-F][0-1A-F]$")
    case = bool(re.search(pattern, binString))
    if case:
        return case
    else:
        return False

def binCheck(binString):
    #'^' and '$' match the string exactly
    pattern = re.compile("^([0-1].{15})$")
    case = bool(re.search(pattern, binString))
    if case:
        return case
    else:
        return False

def hexCheck(hexString):
    #'^' and '$' match the string exactly
    pattern1 = re.compile("^([x][0-9a-f][0-9a-f][0-9a-f][0-9a-f])$")
    case1 = bool(re.search(pattern1, hexString))
    if case1:
        return case1
    else:
        return False

def driver(hexString, binString, pc):
    if hexString != "":
        if 'x' not in hexString.lower():
            hexString = "x" + hexString
        if hexCheck(hexString.lower()):
            # return hexString without the x and as uppercase.
            return hexString.upper()[1:]
        else:
            return "Something wrong with format of hex-value."
    elif binString != "":
        if binCheck(binString):
            return binString
        else:
            return "Something wrong with format of binary value."
    elif pc != "":
        if pcCheck(pc.upper()):
            return pc.upper()
        else:
            return "Something wrong with format of the PC counter hex-value."
    else:
        return "Something is wrong. No input was given."

driver("0xffff","0001 0000 0001 1111","x3000")
