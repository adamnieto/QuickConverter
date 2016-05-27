import re
"""
Author: Adam Nieto

"""
def pcCheck(pc):
    #'^' and '$' match the string exactly
    pattern = re.compile("^([X][0-9A-F][0-9A-F][0-9A-F][0-9A-F])$")
    case = bool(re.search(pattern, pc))
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

def hexDriver(hexString):
    if hexString != "":
        if 'x' not in hexString.lower():
            hexString = "x" + hexString
        if hexCheck(hexString.lower()):
            # return hexString without the x and as uppercase.
            return hexString.upper()[1:]
        else:
            return "ERR: Something wrong with format of hex-value."
    else:
        return "ERR: There was no input! Please try again."
def binDriver(binString):
    if binString != "":
        if binCheck(binString):
            return binString
        else:
            return "ERR: Something wrong with format of binary value. It must be exactly 16 digits long."
    else:
        return "ERR: There was no input for Binary! Please try again."
def pcDriver(pc):
    if pc != "":
        if pcCheck(pc.upper()):
            return pc.upper()
        else:
            return "ERR: Something wrong with format of the PC counter hex-value."
    else:
        return ""
