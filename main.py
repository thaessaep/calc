from flask import Flask, render_template, url_for, request
import json
import generation
import xlrd
import createData


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return post()
    else:
        return render_template("index.html")


def post():
    for key in request.form:
        if request.form[key] == 'True':  # if was click on button
            data = createData.pdfData(xls)
            if key == 'genKP':
                return generation.genKP(data, request.form['clientName'], request.form['requisites'])
            elif key == 'genContract':
                return generation.genContract(data, request.form['requisites'], request.form['clientName'])
    else:  # if user write value
        data = createData.switchData(xls)
        return json.dumps(data)  # return result of values


book = xlrd.open_workbook('static/Прайс_CoreDataNet_03_08_20.xlsx')  # open workbook
xls = book.sheet_by_name('Лист1')  # read workbook by name


if __name__ == "__main__":
    app.run(debug=True)
