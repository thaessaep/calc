

def multiCore(xls, numerous):  # результат цены для ядер
    value = find_name(xls, "Ядра")
    res = numerous * value
    return res


def multiRAM(xls, ram):  # результат цены для оперативки
    if ram <= 30:
        value = find_name(xls, "ОЗУ до 30ГБ")
    elif ram >= 31:
        value = find_name(xls, "ОЗУ от 31ГБ")
    res = ram * value
    return res


def SXD(xls, numerous):  # объём дискового пространства
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


def find_name(xls, name):  # поиск нужного пункта в списке и возврат его стоимости
    value1 = -1  # переменная для подсчёта стобцов
    value2 = -1
    for price in xls.row(1):  # поиск стоблца(Услуги)
        if price.value == 1:
            value2 += 1
            break
    for j in range(0, xls.nrows):
        if xls.cell_value(j, value2) == name:
            for price in xls.row(1):  # поиск стоблца(Цены)
                value1 += 1
                if price.value == 2:
                    return xls.cell_value(j, value1)
    return -1


def switch_dict(xls, x, value):  # switch в python(возвращает значение, посчитанное с excel)
    if x == "core":
        return multiCore(xls, value)
    elif x == "ram":
        return multiRAM(xls, value)
    elif x == "sata":
        return SXD(xls, value)
    elif x == "sas":
        return SXD(xls, value)
    elif x == "ssd":
        return SXD(xls, value)