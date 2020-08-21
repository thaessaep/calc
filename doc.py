from docxtpl import DocxTemplate


wdFormatText = 17  # код pdf-документа


def docx(core, ram, hdd):
    document = DocxTemplate("MainDataNet.docx")  # читает шаблон docx документа
    info = {
        'company': 'Имя компании?',
        'director': 'Имя заказчика?',
        'name': "Кто-то?",
        'core': core,
        'ram': ram,
        'hdd': hdd,
    }
    document.render(info)  # редактирует шаблон
    document.save('MainDataNetResult.docx')
    # convert(r"test.docx", r"D:/Calc/dynamic/MainDataNetResult.pdf")
