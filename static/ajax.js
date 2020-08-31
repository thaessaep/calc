const xhr = new XMLHttpRequest();


function sendRequest(){
    $.ajax({
        url: "http://127.0.0.1:5000/",
        method: "POST",
        data : {
            'core': $('#coreoutput').val(),
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

    $('#coreoutput').change(sendRequest);

    $('#ramoutput').change(sendRequest);

    $('#sataoutput').change(sendRequest);

    $('#sasoutput').change(sendRequest);

    $('#ssdoutput').change(sendRequest);

    $('#coreinput').change(sendRequest);

    $('#raminput').change(sendRequest);

    $('#satainput').change(sendRequest);

    $('#sasinput').change(sendRequest);

    $('#ssdinput').change(sendRequest);

    $('#servNumberId').change(sendRequest)
})
