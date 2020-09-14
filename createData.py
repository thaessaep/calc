import calc_of_value
from flask import request


def switchData(xls):
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
        result.append(total(res, servRes[i]))

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


def pdfData(xls):  # доделать
    result = 0
    length = 0
    value = ""
    for i in request.form:
        if i == 'core' + value:
            length += 1
            value = str(length)
    coreRes = []
    ramRes = []
    sataRes = []
    sasRes = []
    ssdRes = []
    servNumerous = []
    servNumberId = []
    for i in range(0, length):
        if i > 0:
            value = str(i)
        else:
            value = ""
        coreRes.append(int(request.form['core' + value]))
        ramRes.append(int(request.form['ram' + value]))
        sataRes.append(int(request.form['sata' + value]))
        sasRes.append(int(request.form['sas' + value]))
        ssdRes.append(int(request.form['ssd' + value]))
        servNumerous.append(i + 1)
        if request.form['servNumber' + value] == "":
            servNumberId.append(1)
        else:
            servNumberId.append(int(request.form['servNumber' + value]))

    for i in range(0, length):
        res = calc_of_value.multiCore(xls, coreRes[i]) + calc_of_value.multiRAM(xls, ramRes[i]) + \
              calc_of_value.SXD(xls, sataRes[i]) + calc_of_value.SXD(xls, sasRes[i]) + calc_of_value.SXD(xls, ssdRes[i])
        result += res

    data = {
        "core": coreRes,
        "ram": ramRes,
        "sata": sataRes,
        "sas": sasRes,
        "ssd": ssdRes,
        "totalLength": length,
        "servNumerous": servNumerous,
        "servNumber": servNumberId,
        "result": result
    }
    return data


def total(value, servValue):  # total payment amount
    result = value * servValue
    return result
