
def hex2Bin(hexString):
    binNumber = "{0:16b}".format(int(hexString,16))
    # strip any unecessary space from format add 0
    # to front and cut at 16th bit
    return "0" + binNumber.strip(" ")[:17]
print(hex2Bin("5020"))
