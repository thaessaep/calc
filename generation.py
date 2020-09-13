from flask import render_template, send_file
import calc_of_value
import pdfkit


def genKP(xls, data, clientName):
    doc = open("templates/MainDataNetResult.html", "w", encoding="UTF-8")  # open and write new html
    doc.write(render_template("MainDataNet.html", core=data['core'], ram=data['ram'], hdd=hddRes(data),
                              price=resultPdf(xls, data), length=data['totalLength'], servNumerous=data['servNumerous'],
                              clientName=clientName, servNumber=data['servNumber']) + "")
    doc.close()
    return genPdf("templates/MainDataNetResult.html", "pdf/MainDataNetResult.pdf", "MainDataNetResult.pdf")


def genContract(data, clientContract):
    doc = open("templates/virtual_serv_result.html", "w", encoding="UTF-8")
    doc.write(render_template("virtual_serv.html", core=data['core'], ram=data['ram'], servNumerous=data['servNumerous']
                              , hdd=hddRes(data), length=data['totalLength'],
                              clientContract=clientContract, servNumber=data['servNumber']) + "")
    doc.close()
    return genPdf("templates/virtual_serv_result.html", "pdf/virtual_serv_result.pdf", "virtual_serv_result.pdf")


def genPdf(html, pdf, filename):  # convert html in pdf
    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
    options = {'enable-local-file-access': None}  # can convert image
    pdfkit.from_file(html, pdf,
                     configuration=config,
                     options=options)
    return send_file("pdf/" + filename, as_attachment=True)


def hddRes(data):
    hdd = []
    for i in range(0, data['totalLength']):
        hdd.append(data["sata"][i] + data["sas"][i] + data["ssd"][i])
    return hdd


def resultPdf(xls, data):
    result = 0
    for i in range(0, data['totalLength']):
        hdd = calc_of_value.SXD(xls, data["sata"][i]) + \
            calc_of_value.SXD(xls, data["sas"][i]) + calc_of_value.SXD(xls, data["ssd"][i])
        result += calc_of_value.multiCore(xls, data['core'][i]) + calc_of_value.multiRAM(xls, data['ram'][i]) + hdd
    return result
