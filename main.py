from flask import Flask, render_template, url_for, request
import json
import generation
import xlrd
import calc_of_value

app = Flask(__name__)


def switchData():
    totalLength = 0
    core = request.form.getlist(key='core[]')
    ram = request.form.getlist(key='ram[]')
    sata = request.form.getlist(key='sata[]')
    sas = request.form.getlist(key='sas[]')
    ssd = request.form.getlist(key='ssd[]')
    servNumber = request.form.getlist(key='servNumber[]')
    coreRes = []
    ramRes = []
    sataRes = []
    sasRes = []
    ssdRes = []
    result = []
    servRes = []

    for i in core:
        totalLength += 1
        if i != '':
            coreRes.append(calc_of_value.multiCore(xls, int(i)))
        else:
            coreRes.append(0)
    for i in ram:
        if i != '':
            ramRes.append(calc_of_value.multiRAM(xls, int(i)))
        else:
            ramRes.append(0)
    for i in sata:
        if i != '':
            sataRes.append(calc_of_value.SXD(xls, int(i)))
        else:
            sataRes.append(0)
    for i in sas:
        if i != '':
            sasRes.append(calc_of_value.SXD(xls, int(i)))
        else:
            sasRes.append(0)
    for i in ssd:
        if i != '':
            ssdRes.append(calc_of_value.SXD(xls, int(i)))
        else:
            ssdRes.append(0)

    for i in servNumber:
        if i != '':
            servRes.append(int(i))
        else:
            servRes.append(1)

    for i in range(0, totalLength):
        res = coreRes[i] + ramRes[i] + sataRes[i] + sasRes[i] + ssdRes[i]
        result.append(generation.total(res, servRes[i]))

    data = {
        "result": result,
        "coreRes": coreRes,
        "ramRes": ramRes,
        "sataRes": sataRes,
        "sasRes": sasRes,
        "ssdRes": ssdRes,
        "totalLength": totalLength
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
            data = switchData()  # доделать
            if key == 'genKP':
                return generation.genKP(data, request.form['clientName'])
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
