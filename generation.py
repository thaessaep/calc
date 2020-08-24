from flask import request, send_from_directory, render_template
import doc
import calc_of_value


def genKP(xls):
    hdd = int(request.form['sata']) + int(request.form['sas']) + int(request.form['ssd'])
    doc.docx(request.form['core'], request.form['ram'], hdd, total(xls))
    return send_from_directory(directory="dynamic",  # возвращает готовый pdf файл
                               filename="MainDataNetResult.pdf",
                               mimetype='application/pdf')


def genContract():
    return render_template("index.html")


def total(xls):
    result = 0
    for i in request.form:
        if request.form[i] != '' and i != 'genKP' and i != 'genContract':  # проверка на кнопки(genKp...) и на value
            result += calc_of_value.switch_dict(xls, i, int(request.form[i]))
        else:
            continue
    return result