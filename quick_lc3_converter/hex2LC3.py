"""
Author: Adam Nieto
(c) 2016

"""
import re, binascii
# def fltr2Prcs1(binNumber):
#
# def flt1Prcs1(lc3Exprsn, binNumber):
#     fltrPrcs2Access = ["ADD","AND","NOT", ""]
#     registerSeq = binNumber[4:7]
#     registers = {
#               "000":"R0", "001":"R1", "010":"R2", "011":"R3", "100":"R4",
#               "101":"R5", "110":"R6", "111":"R7"
#               }
#     resultExprsn = lc3Exprsn + registers.get(registerSeq, "-1")
#     if resultExprsn is "-1":
#         return False
#     else:
#         fltr1Prcs2(lc3Exprsn, binNumber)
#
# def filters(lc3Exprsn, binNumber):
#     lc3Exprsn = lc3Exprsn + " "
#     fltr1Access = ["ADD","AND","LD","LDI","LDR","LEA","NOT","ST","STI","STR"]
#     fltr2Access = ["JMP","JSR","JSRR","BR"]
#     # These values we automatically know
#     if "TRAP" or "RTI" or "RET" in lc3Exprsn:
#         return lc3Exprsn
#     if lc3Exprsn in fltr1Access:
#         # give only the 3 digits for the DR or SR
#         try:
#             lc3Exprsn += fltr1Prcs1(binNumber)
#         except Exception:
#             print("There is something wrong with the register of your SR or " +
#                   "DR.")
#
#     elif lc3Exprsn in fltr2Access:
#         try:
#             # must be a code with JMP, JSR, JSRR, or BR
#             fltr2Prcs1(lc3Exprsn, binNumber[4:])
#     else:
#         return False
#
# def oppCodes(binNumber):
#     trapVectors = {
#                 "0010 0000":"x20","0010 0001":"x21",
#                 "0010 0010":"x21","0010 0011":"x23",
#                 "0010 0101":"x25"
#                 }
#     specOppCodes = {
#                  "01001":"JSR", "01000": "JSRR"
#                  }
#     lc3OppCodes = {
#                 "0001":"ADD","0101":"AND","0000":"BR",
#                 "1100":"JMP","0100":"JSR","0010":"LD",
#                 "1010":"LDI","0110":"LDR","1110":"LEA",
#                 "1001":"NOT","1100":"RET","1000":"RTI",
#                 "0011":"ST","1011":"STI","0111":"STR"
#                 }
#     #JSR and JSRR checker
#     if binNumber[:3] == "0100":
#         #specOppCodes dictionary is used JSR and JSRR
#         lc3Code = specOppCodes.get(binNumber[:4],"-1")
#         if lc3Code is "-1":
#             return False
#         else:
#             return lc3Code
#     #TRAP Code Checker
#     elif binNumber[:3] == "1111":
#         #trapVectors dictionary is used
#         vector = trapVectors.get(binNumber[:3],"-1")
#         if vector is "-1":
#             return False
#         else:
#             return "TRAP " + vector
#     else:
#         #lc3OppCodes dictionary is used
#         lc3Code = lc3OppCodes.get(binNumber[:3],"-1")
#         if lc3Code is "-1":
#             return False
#         elif lc3Code is "RET" or lc3Code is "RTI":
#             # checking if it is fully the value for RET/RTI
#             if binNumber is "1100000111000000" or "1000000000000000":
#                 return lc3Code
#             else:
#                 return False
#         else:
#             return lc3Code
def trapVectors(vector):
    vectors = {
            "00100000": "x20",
            "00100001": "x21",
            "00100010": "x22",
            "00100011": "x23",
            "00100100": "x24",
            "00100101": "x25",
            }
    result = vectors.get(vector,"-1")
    return result

def getNZP(num):
    nzpDict = {
            "000":"", "100":"n","010":"z", "001":"p", "110":"nz","111":"nzp",
            "011":"zp", "101":"np",
            }
    result = nzpDict.get(num,"-1")
    return result

def bin2Dec(binaryNumber):
    decimal = 0
    index = 0
    for i in binaryNumber[::-1]:
        if i is '1':
            decimal += 2 ** int(index)
        else:
            decimal += 0
        index += 1
    return str(decimal)

def getRegister(registerCand):
    return "R" + bin2Dec(registerCand)

def immdConverter(number):
    if number[0] is '1':
        # need to do two's complement
        result = ""
        indexPos = 0
        indexOfLast1 = 0
        #get rid of the signed bit and reverses string
        for i in number[1:]:
            if i is '1':
                indexOfLast1 = indexPos
            indexPos += 1
        indexPos = 0
        for i in number[1:]:
            if indexPos is not indexOfLast1:
                if i is "1":
                    result += "0"
                else:
                    result += "1"
            else:
                result += "1"
            indexPos += 1
        finalResult = "#-" + bin2Dec(result)
        return finalResult
    else:
        finalResult = "#" + bin2Dec(number)
        return finalResult

def pcOffset(offset, pc):
    number = int(pc) + int(immdConverter(offset)[1:])
    return "x" + str(number)

def checkBinary(binaryNumber):
    criteria = {
		     "^[0].{2}[1][0-1].{5}[0].{2}[0-1].{2}$":'add1',
             "^[0].{2}[1][0-1].{5}[1][0-1].{4}$": "add2",
             "^[0][1][0][1][0-1].{5}[0].{2}[0-1].{2}$":'and1',
             "^[0][1][0][1][0-1].{5}[1][0-1].{4}$": "and2",
             "^[0][0][0][0][0-1].{11}$": "br",
             "^[1][1][0][0][0].{2}[0-1].{2}[0].{5}$":"jmp",
             "^[0][1][0][0][1][0-1].{10}$": "jsr",
             "^[0][1][0][0][0][0].{2}[0-1].{2}[0].{5}$":"jsrr",
             "^[0][0][1][0][0-1].{11}$":"ld",
             "^[1][0][1][0][0-1].{11}$":"ldi",
             "^[0][1][1][0][0-1].{11}$":"ldr",
             "^[1][1][1][0][0-1].{11}$":"lea",
             "^[1][0][0][1][0-1].{5}[1].{5}$":"not",
             "^[1][1][0].{3}[1].{2}[0].{5}]$":"ret",
             "^[1][0].{14}$":"rti",
             "^[0][0][1][1][0-1].{11}$":"st",
             "^[1][0][1][1][0-1].{11}$":"sti",
             "^[0][1][1][1][0-1].{11}$":"str",
             "^[1].{3}[0].{2}[0-1].{7}$":"trap"
             }
    keys = criteria.keys()
    for expression in keys:
        statement = re.compile(expression)
        result = bool(re.search(statement, binaryNumber))
        if result:
            return criteria.get(expression,"-1")

def hex2Bin(hexString):
    binNumber = "{0:16b}".format(int(hexString,16))
    # strip any unecessary space from format add 0
    # to front and cut at 16th bit
    return "0" + binNumber.strip(" ")[:17]


def bin2LC3(hexString, pc):
    lc3Exprsn = ""
    binNum = hex2Bin(hexString).strip(" ")
    getExpression = {
      "add1":"ADD " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + "," + getRegister(binNum[13:16]),
      "add2":"ADD " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + "," + immdConverter(binNum[11:16]),
      "and1":"AND " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + "," + getRegister(binNum[13:16]),
      "and2":"AND " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + "," + immdConverter(binNum[11:16]),
      "br":"BR" + getNZP(binNum[4:7]) + " " + pcOffset(binNum[7:16],pc),
      "jmp":"JMP " + getRegister(binNum[7:10]),
      "jsr":"JSR " + pcOffset(binNum[5:16],pc),
      "jsrr": "JSRR " + getRegister(binNum[7:10]),
      "ld":"LD " + getRegister(binNum[4:7]) + ", " + pcOffset(binNum[7:16],pc),
      "ldi":"LDI " + getRegister(binNum[4:7]) + ", " +
      pcOffset(binNum[7:16],pc),
      "ldr":"LDR " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + "," + immdConverter(binNum[10:16]),
      "lea":"LEA " + getRegister(binNum[4:7]) + ", " +
      pcOffset(binNum[7:16],pc),
      "not":"NOT " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]),
      "ret":"RET",
      "rti":"RTI",
      "st":"ST " + getRegister(binNum[4:7]) + ", " + pcOffset(binNum[7:16],pc),
      "sti":"STI " + getRegister(binNum[4:7]) + ", " +
      pcOffset(binNum[7:16],pc),
      "str":"STR " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + "," + immdConverter(binNum[10:16]),
      "trap":"TRAP" + trapVectors(binNum[8:16])
      }
    binCheck = checkBinary(binNum)
    if binCheck:
        lc3Expression = getExpression.get(binCheck,"-1")
        if lc3Expression is "-1":
            print("Something went wrong.")
        else:
            return lc3Expression
    else:
        return "Incorrect Input."

    # # Getting oppCode
    # try:
    #     lc3Exprsn += oppCodes(binNumber) + '\s'
    # #TODO make sure that this error goes through the gui
    # except Exception:
    #     print("The hexidecimal number provided is an unacceptable value",
    #           "for the LC3.")
    # # Allows for the binary to be filtered through
    # # strip on lc3Exprsn for precaution.
    # result = filters(lc3Exprsn.strip(" "), binNumber)
    # return result

print(bin2LC3("5020","3000"))




#TODO might want to get rid of the get function for dictionaries because will return -1 if false
