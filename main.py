from flask import Flask, render_template, url_for, request, send_from_directory
import json
import generation
import xlrd

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])  # принимает введённые данные пользователя
def index():
    if request.method == "POST":  # принимает значения с формы
        return post()
    else:
        return render_template("index.html")


def post():
    for key in request.form:
        if request.form[key] == 'True':  # если какая-либо кнопка была нажата
            if key == 'genKP':
                return generation.genKP(xls)
            elif key == 'genContract':
                return generation.genContract()
    else:  # если на сайте вводятся значения
        return json.dumps(generation.total(xls))  # возвращает результат для запроса на вывод


book = xlrd.open_workbook('static/Прайс_CoreDataNet_03_08_20.xlsx')  # открытие книги
xls = book.sheet_by_name('Лист1')  # чтение книги по названию


if __name__ == "__main__":
    app.run(debug=True)
