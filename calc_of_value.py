
def multiCore(xls, numerous):  # result price for cores
    value = find_name(xls, "Ядра")
    res = numerous * value
    return res


def multiRAM(xls, ram):  # result price for ram
    if ram <= 30:
        value = find_name(xls, "ОЗУ до 30ГБ")
    elif ram >= 31:
        value = find_name(xls, "ОЗУ от 31ГБ")
    res = ram * value
    return res


def SXD(xls, numerous):  # result price for ssd, sata, sas
    if numerous < 21:
        value = find_name(xls, "СХД до 20ГБ")
    elif numerous <= 100:
        value = find_name(xls, "СХД  от 21 до 100ГБ")
    elif numerous <= 1000:
        value = find_name(xls, "СХД  от 101ГБ  до 1ТБ")
    elif numerous > 1000:
        res = 0  # 0 contract price(договорная цена)
        return res
    res = numerous * value
    return res


def find_name(xls, name):  # search name of column and return value
    value1 = -1  # variable for column counting(подсчёта стобцов)
    value2 = -1
    for price in xls.row(1):  # search column(Услуги)
        if price.value == 1:
            value2 += 1
            break
    for j in range(0, xls.nrows):
        if xls.cell_value(j, value2) == name:
            for price in xls.row(1):  # search column(Цены)
                value1 += 1
                if price.value == 2:
                    return xls.cell_value(j, value1)
    return -1
