const xhr = new XMLHttpRequest();


function sendRequest(){
    $.ajax({
        url: "http://127.0.0.1:5000/",
        method: "POST",
        data : {
            'core': $('#core-id').val(),
            'ram': $('#ram-id').val(),
            'sata': $('#sata-id').val(),
            'sas': $('#sas-id').val(),
            'ssd': $('#ssd-id').val(),
        },
        success: function (result) { // принимает значение с Python и парсит его
            result = $.parseJSON(result)
            $('#result').text(result)
        },
        error: function () { // выводит ошибку, если значение не дошло до функции
            alert("Bad")
        }
    })
}


$(document).ready(function () { // когда документ готов к работе, то начинать проверку изменений

    $('#core-id').change(sendRequest);

    $('#ram-id').change(sendRequest);

    $('#sata-id').change(sendRequest);

    $('#sas-id').change(sendRequest);

    $('#ssd-id').change(sendRequest);

})
