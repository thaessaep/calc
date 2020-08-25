from flask import request, send_from_directory, redirect
import doc
import calc_of_value


def genKP(xls):
    doc.docxData(request.form['core'], request.form['ram'], hddRes(), total(xls))
    return redirect("/pdf1", code=302)  # код 302 - пост-запрос


def genContract(xls):
    doc.docxServ(request.form['core'], request.form['ram'], hddRes(), total(xls))
    return redirect("/pdf2", code=302)  # код 302 - пост-запрос


def hddRes():
    hdd = int(request.form['sata']) + int(request.form['sas']) + int(request.form['ssd'])
    return hdd


def total(xls):
    result = 0
    for i in request.form:
        if request.form[i] != '' and i != 'genKP' and i != 'genContract':  # проверка на кнопки(genKp...) и на value
            result += calc_of_value.switch_dict(xls, i, int(request.form[i]))
        else:
            continue
    return result
