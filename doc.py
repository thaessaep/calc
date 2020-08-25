from docxtpl import DocxTemplate
from docx2pdf import convert


def docxData(core, ram, hdd, price):
    document = DocxTemplate("docx/MainDataNet.docx")  # читает шаблон docx документа
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
    document.save('docx/MainDataNetResult.docx')
    convert(r"D:\Calc\docx\MainDataNetResult.docx", r"D:\Calc\pdf\MainDataNetResult.pdf")


def docxServ(core, ram, hdd, price):
    document = DocxTemplate("docx/virtual_serv.docx")  # читает шаблон docx документа
    info = {
        'price': price,
        'core': core,
        'ram': ram,
        'hdd': hdd,
    }
    document.render(info)  # редактирует шаблон
    document.save('docx/virtual_serv_result.docx')
    convert(r"D:\Calc\docx\virtual_serv_result.docx", r"D:\Calc\pdf\virtual_serv_result.pdf")
