from flask import Flask, render_template, url_for, request
import json
import generation
import xlrd
import calc_of_value

app = Flask(__name__)


def switchData():
    if request.form['core'] != '':
        coreRes = calc_of_value.multiCore(xls, int(request.form['core']))
    else:
        coreRes = 0
    if request.form['ram'] != '':
        ramRes = calc_of_value.multiRAM(xls, int(request.form['ram']))
    else:
        ramRes = 0
    if request.form['sata'] != '':
        sataRes = calc_of_value.SXD(xls, int(request.form['sata']))
    else:
        sataRes = 0
    if request.form['sas'] != '':
        sasRes = calc_of_value.SXD(xls, int(request.form['sas']))
    else:
        sasRes = 0
    if request.form['ssd'] != '':
        ssdRes = calc_of_value.SXD(xls, int(request.form['ssd']))
    else:
        ssdRes = 0
    data = {
        "result": generation.total(xls),
        "coreRes": coreRes,
        "ramRes": ramRes,
        "sataRes": sataRes,
        "sasRes": sasRes,
        "ssdRes": ssdRes
    }
    return data


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return post()
    else:
        return render_template("index.html")


def post():
    for key in request.form:
        if request.form[key] == 'True':  # if was click on button
            if key == 'genKP':
                return generation.genKP(request.form['core'], request.form['ram']
                                        , generation.total(xls), request.form['clientName'])
            elif key == 'genContract':
                return generation.genContract(request.form['core']
                                              , request.form['ram'], request.form['clientContract'])
    else:  # if user write value
        data = switchData()
        return json.dumps(data)  # return result of values


book = xlrd.open_workbook('static/Прайс_CoreDataNet_03_08_20.xlsx')  # open workbook
xls = book.sheet_by_name('Лист1')  # read workbook by name

if __name__ == "__main__":
    app.run(debug=True)
