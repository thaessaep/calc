from flask import request, send_from_directory, render_template
import calc_of_value
import pdfkit


def genKP(core, ram, price):
    doc = open("templates/MainDataNetResult.html", "w", encoding="UTF-8")  # open and write new html
    doc.write(render_template("MainDataNet.html", core=core, ram=ram, hdd=hddRes(), price=price)+"")
    doc.close()
    return genPdf("templates/MainDataNetResult.html", "pdf/MainDataNetResult.pdf", "MainDataNetResult.pdf")


def genContract(core, ram):
    doc = open("templates/virtual_serv_result.html", "w", encoding="UTF-8")
    doc.write(render_template("virtual_serv.html", core=core, ram=ram, hdd=hddRes()) + "")
    doc.close()
    return genPdf("templates/virtual_serv_result.html", "pdf/virtual_serv_result.pdf", "virtual_serv_result.pdf")


def genPdf(html, pdf, filename):  # convert html in pdf
    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
    options = {'enable-local-file-access': None}  # can convert image
    pdfkit.from_file(html, pdf,
                     configuration=config,
                     options=options)
    return send_from_directory(directory="pdf",  # return ready pdf
                               filename=filename,
                               mimetype='application/pdf')


def hddRes():
    hdd = int(request.form['sata']) + int(request.form['sas']) + int(request.form['ssd'])
    return hdd


def total(xls):  # total payment amount
    result = 0
    for i in request.form:
        if request.form[i] != '' and i != 'genKP' and i != 'genContract':  # check button(genKp...) and value
            result += calc_of_value.switch_dict(xls, i, int(request.form[i]))
        else:
            continue
    return result
