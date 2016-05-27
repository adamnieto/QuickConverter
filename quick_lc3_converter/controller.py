from os import getenv
from flask import Flask, render_template, request, url_for, Markup
from flask.ext.bower import Bower
from quick_lc3_converter.toLC3Converter import hex2LC3, bin2LC3, hex2Bin, bin2Hex, hex2Dec, signedBin2Dec
from quick_lc3_converter.inputValidation import hexDriver, binDriver, pcDriver

"""
Author: Adam Nieto

"""

errorStatus = ""


def getErrorStatus():
    global errorStatus
    tempStatus = errorStatus
    return tempStatus

def module1():
    global errorStatus
    errorBox1 = ""
    hex2LC3Box1 = request.form["hexLC3Box1"]
    pcBox1 = request.form["pcBox1"]
    hex2LC3Box2 = ""
    inputVald1 = hexDriver(hex2LC3Box1)
    inputVald2 = pcDriver(pcBox1)
    if "ERR" in inputVald1 or "ERR" in inputVald2:
        errorStatus = "error1"
        if "ERR" in inputVald1 and "ERR" in inputVald2:
            errorBox1 = inputVald1 + "\n" + inputVald2
            return errorBox1
        elif "ERR" in inputVald1:
            errorBox1 = inputVald1
            return errorBox1
        else:
            errorBox1 = inputVald2
            return errorBox1
    else:
        global errorStatus
        result = hex2LC3(hex2LC3Box1, pcBox1)
        if "ERR" in result:
            errorStatus = 'error1'
            errorBox1 = result
            return errorBox1
        else:
            hex2LC3Box2 = result
            return hex2LC3Box2

def module2():
    global errorStatus
    errorBox2 = ""
    bin2LC3Box1 = request.form["binLC3Box1"]
    pcBox2 = request.form["pcBox2"]
    bin2LC3Box2 = ""
    inputVald1 = binDriver(bin2LC3Box1)
    inputVald2 = pcDriver(pcBox2)
    if "ERR" in inputVald1 or "ERR" in inputVald2:
        errorStatus = "error2"
        errorBox2 = inputVald1 + "\n" + inputVald2
        return errorBox2
    else:
        result = bin2LC3(bin2LC3Box1, pcBox2)
        if "ERR" in result:
            errorStatus = "error2"
            errorBox2 = result
            return errorBox2
        else:
            bin2LC3Box2 = result
            return bin2LC3Box2

def module3():
    global errorStatus
    errorBox3 = ""
    hex2BinBox1 = request.form["hexBinBox1"]
    hex2BinBox2 = ""
    inputVald = hexDriver(hex2BinBox1)
    if "ERR" in inputVald:
        errorStatus = "error3"
        errorBox3 = inputVald
        return errorBox3
    else:
        result = hex2Bin(hex2BinBox1)
        if "ERR" in result:
            errorStatus = "error3"
            errorBox3 = result
            return errorBox3

        else:
            hexBinBox2 = result
            return hexBinBox2

def module4():
    global errorStatus
    errorBox4 = ""
    bin2HexBox1 = request.form["binHexBox1"]
    bin2HexBox2 = ""
    inputVald = binDriver(bin2HexBox1)
    if "ERR" in inputVald:
        errorStatus = "error4"
        errorBox4 = inputVald
        return errorBox4
    else:
        result = bin2Hex(bin2HexBox1)
        if "ERR" in result:
            errorStatus = "error4"
            errorBox4 = result
            return errorBox4
        else:
            bin2HexBox2 = result
            return bin2HexBox2

def module5():
    global errorStatus
    errorBox5 = ""
    hex2DecBox1 = request.form["hexDecBox1"]
    hex2DecBox2 = ""
    inputVald = hexDriver(hex2DecBox1)
    if "ERR" in inputVald:
        errorStatus = "errorBox5"
        errorBox5 = inputVald
        return errorBox5
    else:
        result = hex2Dec(hex2DecBox1)
        if "ERR" in result:
            errorStatus = "errorBox5"
            errorBox5 = result
            return errorBox5
        else:
            hex2DecBox2 = result
            return hex2DecBox2

def module6():
    global errorStatus
    errorBox6 = ""
    bin2DecBox1 = request.form["binDecBox1"]
    bin2DecBox2 = ""
    inputVald = binDriver(bin2DecBox1)
    if "ERR" in inputVald:
        errorStatus = "error6"
        errorBox6 = inputVald
        return errorBox6
    else:
        result = signedBin2Dec(bin2DecBox1)
        if "ERR" in result:
            errorStatus = "error6"
            errorBox6 = result
            return errorBox6
        else:
            bin2DecBox2 = result
            return bin2DecBox2
