import re

def pcCheck(pc):
    #'^' and '$' match the string exactly
    pattern = re.compile("^[0-1A-F]{4}$")
    case = bool(re.search(pattern, binString))
    if case:
        return case
    else:
        return False

def binCheck(binString):
    #'^' and '$' match the string exactly
    pattern = re.compile("^[0-1]{16}$")
    case = bool(re.search(pattern, binString))
    if case:
        return case
    else:
        return False

def hexCheck(hexString):
    #'^' and '$' match the string exactly
    pattern1 = re.compile("^0[x][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$")
    case1 = bool(re.search(pattern1, hexString))
    if case1:
        return case1
    else:
        return False

def driver(hexString, binString, pc):
    if hexString != "":
        if hexCheck(hexString.lower()):
            return hexString
        else:
            return "-1"
    elif binString != "":
        if "0x" not in binString:
            binString = "0x" + binString
        if binCheck(binString):
            return binString
        else:
            return "-1"
    elif pc != "":
        if pcCheck(pc.upper())
    else:
        # This means no input was given just empty strings
        return "-2"

driver("0xffff","0001 0000 0001 1111","x3000")
