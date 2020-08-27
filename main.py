from flask import Flask, render_template, url_for, request
import json
import generation
import xlrd

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return post()
    else:
        return render_template("index.html")


def post():
    for key in request.form:
        if request.form[key] == 'True':  # if was click on button если какая-либо кнопка была нажата
            if key == 'genKP':
                return generation.genKP(request.form['core'], request.form['ram'], generation.total(xls))
            elif key == 'genContract':
                return generation.genContract(request.form['core'], request.form['ram'])
    else:  # if user write value
        return json.dumps(generation.total(xls))  # return result of values


book = xlrd.open_workbook('static/Прайс_CoreDataNet_03_08_20.xlsx')  # open workbook
xls = book.sheet_by_name('Лист1')  # read workbook by name

if __name__ == "__main__":
    app.run(debug=True)
