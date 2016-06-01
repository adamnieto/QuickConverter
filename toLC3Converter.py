import re
"""
Author: Adam Nieto

TODO: Might want to get rid of the get function for dictionaries because will
      return -1 if false.
TODO: Make sure that this error goes through the gui
"""

def simplifyTraps(expression):
    simplify = {
             "TRAP x20":"GETC", "TRAP x21":"OUT", "TRAP x22":"PUTS",
             "TRAP x23":"IN", "TRAP x24":"PUTSP", "TRAP x25":"HALT",
             }
    result = simplify.get(expression,"-1")
    return result

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
            "000":"",
            "100":"n",
            "010":"z",
            "001":"p",
            "110":"nz",
            "111":"nzp",
            "011":"zp",
            "101":"np",
            }
    result = nzpDict.get(num,"-1")
    return result

def getRegister(registerCand):
    return "R" + bin2Dec(registerCand)

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

def signedBin2Dec(number):
    if number[0] is '1':
        # need to do two's complement!
        # zero needs to be there because
        # we take away the signed bit;
        # will mess up value if missing signed bit
        result = "0"
        # get rid of the signed bit
        numTemp = number[1:]
        # looping over string backwards
        indexPos = len(numTemp) - 1
        indexOfLast1 = 0
        while indexPos >= 0:
            i = numTemp[indexPos]
            if i is '1':
                indexOfLast1 = indexPos
                break
            else:
                indexPos -= 1
        # reset indexPos counter for next loop which rebuilds string
        indexPos = 0
        for i in numTemp:
            if indexPos < indexOfLast1:
                # flipping the bits
                if i is "1":
                    result += "0"
                else:
                    result += "1"
            else:
                # keep the 1 there (adding 1)
                result += i

            indexPos += 1
        finalResult = "#-" + bin2Dec(result)
        return finalResult
    else:
        finalResult = "#" + bin2Dec(number)
        return finalResult

def pcOffset(offset, pc):
    if "x" in pc or "X" in pc:
        pc = pc[1:]
    pcFinal = hex2Bin(pc)
    result = hex(int(pcFinal,2) + int(offset, 2))[2:].upper()
    # converts to decimal then converts to hex
    # offsetFinal = int(hex(int(signedBin2Dec(offset)[1:]))[2:], 16)
    return "x" + str(result)

def checkBinary(binaryNumber):
    criteria = {
		     "^([0][0][0][1])([0-1].{5})([0].{2})([0-1].{2})$":'add1',
             "^([0][0][0][1])([0-1].{5})([1])([0-1].{4})$": "add2",
             "^([0][1][0][1])[0-1].{5}[0].{2}[0-1].{2}$":'and1',
             "^([0][1][0][1])[0-1].{5}[1][0-1].{4}$": "and2",
             "^([0][0][0][0])[0-1].{11}$": "br",
             "^([1][1][0][0])([0].{2})([0-1].{2})([0].{5})$":"jmp",
             "^([0][1][0][0])[1][0-1].{10}$": "jsr",
             "^([0][1][0][0])([0][0][0])([0-1].{2})([0].{5})$":"jsrr",
             "^([0][0][1][0])([0-1].{11})$":"ld",
             "^([1][0][1][0])([0-1].{11})$":"ldi",
             "^([0][1][1][0])([0-1].{11})$":"ldr",
             "^([1][1][1][0])([0-1].{11})$":"lea",
             "^([1][0][0][1])([0-1].{5})([1].{5})$":"not",
             "^([1][1][0][0])([0].{2})([1][1][1])([0].{5})$":"ret",
             "^([1][0][0][0])([0].{11})$":"rti",
             "^([0][0][1][1])([0-1].{11})$":"st",
             "^([1][0][1][1])([0-1].{11})$":"sti",
             "^([0][1][1][1])([0-1].{11})$":"str",
             "^([1][1][1][1])([0][0][0][0])([0-1].{7})$":"trap"
             }
    keys = criteria.keys()
    answer = ""
    for expression in criteria:
        statement = re.compile(expression)
        result = bool(re.search(statement, binaryNumber.strip(" ")))
        if result:
            answer = criteria.get(expression,"-1")
    return answer

def bin2Hex(binNum):
    result = "x" + hex(int(binNum, 2))[2:].upper()
    return result

def hex2Bin(hexString):
    if "x" in hexString or "X" in hexString:
        temp = hexString.upper()[1:]
    else:
        temp = hexString.upper()
    hexDecode = {
              "A":"10",
              "B":"11",
              "C":"12",
              "D":"13",
              "E":"14",
              "F":"15"
              }
    binList =  []
    for character in temp:
        if character in hexDecode:
            binList.append(hexDecode.get(character, ""))
        else:
            binList.append(character)
    binary = ""
    for i in binList:
        binaryVersion = bin(int(i))[2:]
        if len(binaryVersion) < 4:
            numOfZeros = 4 - len(binaryVersion)
            binary += numOfZeros * "0" + binaryVersion
        else:
            binary += binaryVersion
    return binary

def hex2Dec(hexString):
    binNum = hex2Bin(hexString)
    result = signedBin2Dec(binNum)[1:]
    return result

def bin2LC3(binNum, pc):
    lc3Exprsn = ""
    getExpression = {
      "add1":"ADD " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + ", " + getRegister(binNum[13:16]),
      "add2":"ADD " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + ", " + signedBin2Dec(binNum[11:16]),
      "and1":"AND " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + ", " + getRegister(binNum[13:16]),
      "and2":"AND " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + ", " + signedBin2Dec(binNum[11:16]),
      "br":"BR" + getNZP(binNum[4:7]) + " " + pcOffset(binNum[7:16],pc),
      "jmp":"JMP " + getRegister(binNum[7:10]),
      "jsr":"JSR " + pcOffset(binNum[5:16],pc),
      "jsrr": "JSRR " + getRegister(binNum[7:10]),
      "ld":"LD " + getRegister(binNum[4:7]) + ", " + pcOffset(binNum[7:16],pc),
      "ldi":"LDI " + getRegister(binNum[4:7]) + ", " +
      pcOffset(binNum[7:16],pc),
      "ldr":"LDR " + getRegister(binNum[4:7]) + ", " +
      getRegister(binNum[7:10]) + ", " + signedBin2Dec(binNum[10:16]),
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
      getRegister(binNum[7:10]) + ", " + signedBin2Dec(binNum[10:16]),
      "trap":simplifyTraps("TRAP " + trapVectors(binNum[8:16]))
      }
    binCheck = checkBinary(binNum)
    if binCheck:
        lc3Expression = getExpression.get(binCheck,"-1")
        if lc3Expression is "-1":
            print("ERR: Something went wrong in the code.")
            return "ERR: Something went wrong in the calculation. Please report to admin."
        else:
            return lc3Expression
    else:
        return "ERR: Something is wrong with the format of the input."

def hex2LC3(hexString, pc):
    binNum = hex2Bin(hexString).strip(" ")
    return bin2LC3(binNum, pc)
