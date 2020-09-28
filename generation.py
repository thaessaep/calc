from flask import render_template, send_file
import pdfkit
import createRecord


def genKP(data, clientName):
    doc = open("templates/MainDataNetResult.html", "w", encoding="UTF-8")  # open and write new html
    doc.write(render_template("MainDataNet.html", data=data, hdd=hddRes(data), clientName=clientName) + "")
    doc.close()
    return genPdf(clientName, "templates/MainDataNetResult.html", "pdf/" + clientName + "KP.pdf",
                  clientName + "KP.pdf", "KP")


def genContract(data, request, clientName, INN):
    doc = open("templates/virtual_serv_result.html", "w", encoding="UTF-8")
    doc.write(render_template("virtual_serv.html", hdd=hddRes(data), form=request,
                              requisites=INN, data=data) + "")
    doc.close()
    return genPdf(clientName, "templates/virtual_serv_result.html", "pdf/" + clientName + "CONT.pdf",
                  clientName + "CONT.pdf", "CONT")


def genPdf(clientName, html, pdf, filename, fileType):  # convert html in pdf
    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
    options = {'enable-local-file-access': None}  # can convert image
    pdfkit.from_file(html, pdf,
                     configuration=config,
                     options=options)
    createRecord.createBase(clientName, pdf, fileType)
    return send_file("pdf/" + filename, as_attachment=True)


def hddRes(data):
    hdd = []
    for i in range(0, data['totalLength']):
        hdd.append(data["sata"][i] + data["sas"][i] + data["ssd"][i])
    return hdd
