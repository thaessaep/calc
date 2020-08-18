from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import xlrd
import json

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])  # принимает введённые данные пользователя
def index():
    if request.method == "POST":  # принимает значения с формы
        # encoder = json.dumps()
        result = 0
        for i in request.form:
            if request.form[i] != '':
                result += switch_dict(i, int(request.form[i]))
            else:
                continue
        return json.dumps(result)
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
    value = 252
    res = numerous * value
    return res


def multiRAM(ram):  # результат цены для оперативки
    if ram <= 30:
        value = 216
    elif ram >= 31:
        value = 100
    res = ram * value
    return res


def SXD(numerous):  # объём дискового пространства
    if numerous < 21:
        value = 6
    elif numerous <= 100:
        value = 2
    elif numerous <= 1000:
        value = 1.5
    elif numerous > 1000:
        res = 0  # 0 значит договорную цену
        return res
    res = numerous * value
    return res


def find_name(ws, name):  # поиск нужного пункта в списке и возврат его стоимости
    value1 = -1  # переменная для подсчёта стобцов
    value2 = -1
    for price in ws.row(1):  # поиск стоблца(Услуги)
        if price.value == 1:
            value2 += 1
            break
    for j in range(0, ws.nrows):
        if ws.cell_value(j, value2) == name:
            for price in ws.row(1):  # поиск стоблца(Цены)
                value1 += 1
                if price.value == 2:
                    return ws.cell_value(j, value1)
    return -1


if __name__ == "__main__":
    app.run(debug=True)
