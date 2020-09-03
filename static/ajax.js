const xhr = new XMLHttpRequest();

let i = 0

function addServ(){
    i++
    // $('.serv').clone(true).appendTo($('.virtual'))

    let test = $('.input1').clone(true).attr({'id': 'coreInput'+i,
        'oninput': 'coreOutput'+i+'.value = coreInput'+i+'.value'})
    let test1 = $('.input2').clone(true).attr({'id': 'coreOutput'+i,
        'oninput': 'coreInput'+i+'.value = coreOutput'+i+'.value'})
    let test2 = $('.coreRes').clone(true).attr('id', 'coreRes'+i)

    test.attr({'id': 'coreInput'+i, 'oninput': 'coreOutput'+i+'.value = coreInput'+i+'.value'})
    test1.attr({'id': 'coreOutput'+i, 'oninput': 'coreInput'+i+'.value = coreOutput'+i+'.value'})
    test2.attr('id', 'coreRes'+i)

    test.appendTo($('.virtual'))
    test1.appendTo($('.virtual'))
    test2.appendTo($('.virtual'))

}


function sendRequest(){
    $.ajax({
        url: "http://127.0.0.1:5000/",
        method: "POST",
        data : {
            'core': $('#coreOutput').val(),
            'ram': $('#ramoutput').val(),
            'sata': $('#sataoutput').val(),
            'sas': $('#sasoutput').val(),
            'ssd': $('#ssdoutput').val(),
            'clientName': $('#clientNameId').val(),
            'clientContract': $('#clientContractId').val(),
            'clientRequisites': $('#clientRequisitesId').val(),
            'servName': $('#servNameId').val(),
            'servNumber': $('#servNumberId').val()
        },
        success: function (res) { // принимает значение с Python и парсит его
            res = $.parseJSON(res)
            result = res["result"]
            coreRes = res["coreRes"]
            ramRes = res["ramRes"]
            sataRes = res["sataRes"]
            sasRes = res["sasRes"]
            ssdRes = res["ssdRes"]
            $('#result').text(result)
            $('#coreRes').text(coreRes)
            $('#ramRes').text(ramRes)
            $('#sataRes').text(sataRes)
            $('#sasRes').text(sasRes)
            $('#ssdRes').text(ssdRes)
        },
        error: function () { // выводит ошибку, если значение не дошло до функции
            alert("Bad")
        }
    })
}


$(document).ready(function () { // когда документ готов к работе, то начинать проверку изменений

    $('#coreOutput').change(sendRequest);

    $('#ramoutput').change(sendRequest);

    $('#sataoutput').change(sendRequest);

    $('#sasoutput').change(sendRequest);

    $('#ssdoutput').change(sendRequest);

    $('#coreInput').change(sendRequest);

    $('#raminput').change(sendRequest);

    $('#satainput').change(sendRequest);

    $('#sasinput').change(sendRequest);

    $('#ssdinput').change(sendRequest);

    $('#servNumberId').change(sendRequest)

    $('#addServId').click(addServ)
})
