from flask import request, send_from_directory, render_template, send_file
import calc_of_value
import pdfkit


def genKP(core, ram, price, clientName):
    doc = open("templates/MainDataNetResult.html", "w", encoding="UTF-8")  # open and write new html
    doc.write(render_template("MainDataNet.html", core=core, ram=ram
                              , hdd=hddRes(), price=price, clientName=clientName)+"")
    doc.close()
    return genPdf("templates/MainDataNetResult.html", "pdf/MainDataNetResult.pdf", "MainDataNetResult.pdf")


def genContract(core, ram, clientContract):
    doc = open("templates/virtual_serv_result.html", "w", encoding="UTF-8")
    doc.write(render_template("virtual_serv.html", core=core, ram=ram
                              , hdd=hddRes(), clientContract=clientContract) + "")
    doc.close()
    return genPdf("templates/virtual_serv_result.html", "pdf/virtual_serv_result.pdf", "virtual_serv_result.pdf")


def genPdf(html, pdf, filename):  # convert html in pdf
    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
    options = {'enable-local-file-access': None}  # can convert image
    pdfkit.from_file(html, pdf,
                     configuration=config,
                     options=options)
    return send_file("pdf/"+filename, as_attachment=True)


def hddRes():
    hdd = int(request.form['sata']) + int(request.form['sas']) + int(request.form['ssd'])
    return hdd


def total(value, servValue):  # total payment amount
    result = value * servValue
    return result
