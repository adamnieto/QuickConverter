"""
Author: Adam Nieto
(c) 2016

"""
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

def hex2Bin(hexString):
    binNumber =  bin(int(hexString, 16))
    return binNumber[2:] # cut off the '0b' of the string

def bin2LC3(hexString):
    lc3Exprsn = ""
    binNumber = hex2Bin(hexString).strip(" ")
    # Getting oppCode
    try:
        lc3Exprsn += oppCodes(binNumber) + '\s'
    #TODO make sure that this error goes through the gui
    except Exception:
        print("The hexidecimal number provided is an unacceptable value",
              "for the LC3.")
    # Allows for the binary to be filtered through
    # strip on lc3Exprsn for precaution.
    result = filters(lc3Exprsn.strip(" "), binNumber)
    return result

bin2LC3()
