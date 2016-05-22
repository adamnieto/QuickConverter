import re

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
def lc3Check(lc3String):
    #'^' and '$' match the string exactly

    #put the patterns in a list and then iterate over them in re.compile and

    #TODO Make sure to strip any spaces while matching. that is how regex has it.
    #TODO make sure to have something for hex values. So while it checks for '#-16 - #15' also have those acceptable values in hex after the patterns four loop.
    patterns =
    {
        "^[ADD][R][0-7][,][R][0-7][,][#]-[1-16]$":'add1',
        "^[ADD][R][0-7][,][R][0-7][,][#][0-15]$": "add2",
        "^[ADD][R][0-7][,][R][0-7][,][R][0-7]$": "add3",
        "^[AND][R][0-7][,][R][0-7][,][#]-[1-16]$":'and1',
        "^[AND][R][0-7][,][R][0-7][,][#][0-15]$": "and2",
        "^"






    }


    re.compile(patterns[i])

    # oppCodes = ["ADD", "AND", "BR", "JMP", "JSR", "JSRR", "LD", "LDI", "LDR",
    #             "LEA", "NOT", "RET", "RTI", "ST", "STI", "STR", "TRAP"]
    # splitString = lc3String.split(" ")
    # if splitString[0] in oppCodes and splitString[0] is "NOT":
    #     lc3String = splitString[1:]
    #     case1 = bool(re.search(pattern1, lc3String))
    #     #TODO need to add pattern for lc3 code



def driver(hexString, binString, lc3String):
    if hexString != "":
        if hexCheck(hexString):
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
    else:
        if lc3Check(lc3String):
            return lc3String
        else:
            return "-1"
# TODO: Need to add lc3 validation checker.


    # checkLC3 = LC3Check(lc3String)
driver("0xffff","0001 0000 0001 1111", "ADD R1, R1, #0")
