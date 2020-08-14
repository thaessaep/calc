from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import xlrd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///price.db'  # подключение базы к объекту
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # создание базы


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)

    def __repr__(self):
        return '<Price %r>' % self.id


@app.route("/", methods=['POST', 'GET'])  # принимает введённые данные пользователя
def index():
    if request.method == "POST":
        CORE = int(request.form['core'])  # принимает названия с формы
        RAM = int(request.form['ram'])
        SATA = int(request.form['sata'])
        SAS = int(request.form['sas'])
        SSD = int(request.form['ssd'])
        result1 = multiRAM(RAM)
        result2 = multiCore(CORE)
        result3 = SXD(SATA)
        result4 = SXD(SSD)
        result5 = SXD(SAS)
        res = result1 + result2 + result3 + result4 + result5
        return render_template('index.html', result=res)
    else:
        return render_template("index.html")


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


'''
book = xlrd.open_workbook('Прайс_CoreDataNet_03_08_20.xlsx')  # открытие книги
xls = book.sheet_by_name('Лист1')  # чтение книги по названию
'''


if __name__ == "__main__":
    app.run(debug=True)
