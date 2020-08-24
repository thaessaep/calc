from docxtpl import DocxTemplate
from docx2pdf import convert


wdFormatText = 17  # код pdf-документа


def docx(core, ram, hdd, price):
    document = DocxTemplate("MainDataNet.docx")  # читает шаблон docx документа
    info = {
        'company': 'Имя компании?',
        'director': 'Имя заказчика?',
        'name': "Кто-то?",
        'price': price,
        'core': core,
        'ram': ram,
        'hdd': hdd,
    }
    document.render(info)  # редактирует шаблон
    document.save('MainDataNetResult.docx')
    convert(r"D:\Calc\MainDataNetResult.docx", r"D:\Calc\dynamic\MainDataNetResult.pdf")
