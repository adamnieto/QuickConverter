def hex2Bin(hexString):
    binNumber =  bin(int(hexString, 16))
    print(binNumber[2:]) # cut off the '0b' of the string
