from flask import request, send_from_directory, render_template, redirect
import calc_of_value
import pdfkit


def genKP(core, ram):
    doc = open("templates/MainDataNetResult.html", "w", encoding="UTF-8")
    doc.write(render_template("MainDataNet.html", core=core, ram=ram, hdd=hddRes())+"")
    doc.close()
    return genPdf("templates/MainDataNetResult.html", "pdf/MainDataNetResult.pdf", "MainDataNetResult.pdf")


def genContract(core, ram):
    doc = open("templates/virtual_serv_result.html", "w", encoding="UTF-8")
    doc.write(render_template("virtual_serv.html", core=core, ram=ram, hdd=hddRes()) + "")
    doc.close()
    return genPdf("templates/virtual_serv_result.html", "pdf/virtual_serv_result.pdf", "virtual_serv_result.pdf")


def genPdf(html, pdf, filename):
    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
    options = {'enable-local-file-access': None}  # чтобы мог читать картинки
    pdfkit.from_file(html, pdf,
                     configuration=config,
                     options=options)
    return send_from_directory(directory="pdf",  # возвращает готовый pdf файл
                               filename=filename,
                               mimetype='application/pdf')


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
