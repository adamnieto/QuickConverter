"""Initialize the quief pcOffset(offset, pc):
    if "x" in pc or "X" in pc:
        pc = pc[1:]
    pcFinal = hex2Bin(pc)
    result = hex(int(pcFinal,2) + int(offset, 2))[2:].upper()
    # converts to decimal then converts to hex
    # offsetFinal = int(hex(int(signedBin2Dec(offset)[1:]))[2:], 16)
    return "x" + str(result)
k_lc3_convert app"""
from os import getenv, environ
from flask import Flask, render_template, request, url_for, Markup
from flask.ext.bower import Bower
from controller import module1, module2, module3, module4, module5, module6, getErrorStatus

app = Flask(__name__)
Bower(app)

@app.route('/',  methods=['GET','POST'])
def test():
    """Return the index page for the app"""
    try:
        if request.method == "POST":
            if request.form['button'] == "module1":
                if "ERR" in module1():
                    errorBox1= module1()
                    errorStatus = getErrorStatus()
                    return render_template("hex2LC3.html", errorStatus=errorStatus,
                                                         errorBox1=errorBox1)
                else:
                    hex2LC3Box2 = module1()
                    return render_template("hex2LC3.html", hex2LC3Box2=hex2LC3Box2)

            elif request.form["button"] == "module2":
                if "ERR" in module2():
                    errorBox2 = module2()
                    errorStatus = getErrorStatus()
                    return render_template("bin2LC3.html", errorStatus=errorStatus,
                                                         errorBox2=errorBox2)
                else:
                    bin2LC3Box2 = module2()
                    return render_template("bin2LC3.html", bin2LC3Box2=bin2LC3Box2)

            elif request.form["button"] == "module3":
                if "ERR" in module3():
                    errorBox3 = module3()
                    errorStatus = getErrorStatus()
                    return render_template("hex2Bin.html", errorStatus=errorStatus,
                                                         errorBox3=errorBox3)
                else:
                    hexBinBox2 = module3()
                    print("hello")
                    return render_template("hex2Bin.html", hexBinBox2=hexBinBox2)

            elif request.form["button"] == "module4":
                if "ERR" in module4():
                    errorBox4 = module4()
                    errorStatus = getErrorStatus()
                    return render_template("bin2Hex.html", errorStatus=errorStatus,
                                                         errorBox4=errorBox4)
                else:
                    binHexBox2 = module4()
                    return render_template("bin2Hex.html", binHexBox2=binHexBox2)

            elif request.form["button"] == "module5":
                if "ERR" in module5():
                    errorBox5 = module5()
                    errorStatus = getErrorStatus()
                    return render_template("hex2Dec.html", errorStatus=errorStatus,
                                                         errorBox5=errorBox5)
                else:
                    hexDecBox2 = module5()
                    return render_template("hex2Dec.html", hexDecBox2=hexDecBox2)

            else:
                if "ERR" in module6():
                    errorBox6 = module6()
                    errorStatus = getErrorStatus()
                    return render_template("bin2Dec.html", errorStatus=errorStatus,
                                                         errorBox6=errorBox6)
                else:
                    binDecBox2 = module6()
                    return render_template("bin2Dec.html", binDecBox2=binDecBox2)

        else:
            return render_template("index.html")
    except Exception as err:
        errorBox1 = err
        return render_template("error.html", errorBox1=errorBox1)

if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
