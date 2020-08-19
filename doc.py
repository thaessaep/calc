from docxtpl import DocxTemplate
import docx


def docx(core, ram, hdd):
    document = DocxTemplate("Основа_Дата_Нэт.docx")  # читает шаблон docx документа
    info = {
        'company': '1',
        'director': '2',
        'core': core,
        'ram': ram,
        'hdd': hdd,
    }
    document.render(info)  # редактирует шаблон
    document.save('Основа_Дата_Нэт_результат.docx')
    # a=''
    # fullText = []
    # doc = docx.Document('Основа_Дата_Нэт_результат.docx')
    # for res in doc:
    #     fullText.append(res.text)
    # a = '\n'.join(fullText)
    # print(a)
