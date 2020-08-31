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
    return send_file("pdf/"+filename)
    # return send_from_directory(directory="pdf",  # return ready pdf
    #                            filename=filename,
    #                            mimetype='application/pdf')


def hddRes():
    hdd = int(request.form['sata']) + int(request.form['sas']) + int(request.form['ssd'])
    return hdd


def total(xls):  # total payment amount
    result = 0
    if "servNumber" in request.form and request.form["servNumber"] != '':  # check servNumber
        servValue = int(request.form["servNumber"])
    else:
        servValue = 1
    for i in request.form:
        if request.form[i] != '' and (i == 'core' or i == 'ram' or i == 'sas'
                                      or i == 'sata' or i == 'ssd'):  # check button(genKp...) and value
            result += calc_of_value.switch_dict(xls, i, int(request.form[i]), servValue)
        else:
            continue
    return result
