from flask import Flask, render_template, url_for, request, send_from_directory
import json
import xlrd
import doc

app = Flask(__name__)


book = xlrd.open_workbook('static/Прайс_CoreDataNet_03_08_20.xlsx')  # открытие книги
xls = book.sheet_by_name('Лист1')  # чтение книги по названию


@app.route("/", methods=["POST", "GET"])  # принимает введённые данные пользователя
def index():
    if request.method == "POST":  # принимает значения с формы
        for key in request.form:
            if request.form[key] == 'True':  # если какая-либо кнопка была нажата
                if key == 'genKP':
                    hdd = int(request.form['sata']) + int(request.form['sas']) + int(request.form['ssd'])
                    doc.docx(request.form['core'], request.form['ram'], hdd)
                    return send_from_directory(directory="dynamic",  # возвращает готовый pdf файл
                                               filename="pdf1.pdf",
                                               mimetype='application/pdf')
                elif key == 'genContract':
                    return render_template("index.html")
        else:  # если на сайте вводятся значения
            result = 0
            for i in request.form:
                if request.form[i] != '':
                    result += switch_dict(i, int(request.form[i]))
                else:
                    continue
            return json.dumps(result)  # возвращает результат для запроса на вывод
    else:
        return render_template("index.html")


def switch_dict(x, value):  # switch в python(возвращает значение, посчитанное с excel)
    if x == "core":
        return multiCore(value)
    elif x == "ram":
        return multiRAM(value)
    elif x == "sata":
        return SXD(value)
    elif x == "sas":
        return SXD(value)
    elif x == "ssd":
        return SXD(value)


def multiCore(numerous):  # результат цены для ядер
    value = find_name(xls, "Ядра")
    res = numerous * value
    return res


def multiRAM(ram):  # результат цены для оперативки
    if ram <= 30:
        value = find_name(xls, "ОЗУ до 30ГБ")
    elif ram >= 31:
        value = find_name(xls, "ОЗУ от 31ГБ")
    res = ram * value
    return res


def SXD(numerous):  # объём дискового пространства
    if numerous < 21:
        value = find_name(xls, "СХД до 20ГБ")
    elif numerous <= 100:
        value = find_name(xls, "СХД  от 21 до 100ГБ")
    elif numerous <= 1000:
        value = find_name(xls, "СХД  от 101ГБ  до 1ТБ")
    elif numerous > 1000:
        res = 0  # 0 значит договорную цену
        return res
    res = numerous * value
    return res


def find_name(xl, name):  # поиск нужного пункта в списке и возврат его стоимости
    value1 = -1  # переменная для подсчёта стобцов
    value2 = -1
    for price in xl.row(1):  # поиск стоблца(Услуги)
        if price.value == 1:
            value2 += 1
            break
    for j in range(0, xl.nrows):
        if xl.cell_value(j, value2) == name:
            for price in xl.row(1):  # поиск стоблца(Цены)
                value1 += 1
                if price.value == 2:
                    return xl.cell_value(j, value1)
    return -1


if __name__ == "__main__":
    app.run(debug=True)
