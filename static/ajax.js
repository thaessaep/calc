const xhr = new XMLHttpRequest();

let number = 0

function addServ(){

    number += 1;

    let input = $('#duplicate').clone(true);

    let resInput = input.clone(true).find(':input, output').val("").each(function(){ // clone part of html

        let newId = this.id + number;

        //serv
        if(this.id == 'servNumberId' || this.id == 'servNameId'){
            $(this).attr({'id': newId, 'name': this.name+number});
        }
        else if(this.id == 'servNumerous'){
            $(this).attr('id', newId);
        }

        //core
        else if(this.id == 'coreInput'){
            $(this).attr({'id': newId,'oninput': 'coreOutput'+number+'.value = coreInput'
                    +number+'.value'});
        }
        else if(this.id == 'coreOutput'){
            $(this).attr({'id': newId, 'name': "core"+number,
                'oninput': 'coreInput'+number+'.value = coreOutput'+number+'.value'})
        }

        //ram
        else if(this.id == 'ramInput'){
            $(this).attr({'id': newId,'oninput': 'ramOutput'+number+'.value = ramInput'
                    +number+'.value'});
        }
        else if(this.id == 'ramOutput'){
            $(this).attr({'id': newId, 'name': "ram"+number,
                'oninput': 'ramInput'+number+'.value = ramOutput'+number+'.value'})
        }

        //sata
        else if(this.id == 'sataInput'){
            $(this).attr({'id': newId,'oninput': 'sataOutput'+number+'.value = sataInput'
                    +number+'.value'});
        }
        else if(this.id == 'sataOutput'){
            $(this).attr({'id': newId, 'name': "sata"+number,
                'oninput': 'sataInput'+number+'.value = sataOutput'+number+'.value'})
        }

        //sas
        else if(this.id == 'sasInput'){
            $(this).attr({'id': newId,'oninput': 'sasOutput'+number+'.value = sasInput'
                    +number+'.value'});
        }
        else if(this.id == 'sasOutput'){
            $(this).attr({'id': newId, 'name': "sas"+number,
                'oninput': 'sasInput'+number+'.value = sasOutput'+number+'.value'})
        }

        //ssd
        else if(this.id == 'ssdInput'){
            $(this).attr({'id': newId,'oninput': 'ssdOutput'+number+'.value = ssdInput'
                    +number+'.value'});
        }
        else if(this.id == 'ssdOutput'){
            $(this).attr({'id': newId, 'name': "ssd"+number,
                'oninput': 'ssdInput'+number+'.value = ssdOutput'+number+'.value'})
        }

        //result
        else if(this.id == 'coreRes' || this.id == 'ramRes' || this.id == 'sataRes' || this.id == 'sasRes'
            || this.id == 'ssdRes' || this.id == 'result'){
            $(this).attr('id', newId);
        }


    }).end()

    $('#queue').append(resInput)

}


function sendRequest(){

    let coreOutput = [], ramOutput = [], sataOutput = [], sasOutput = [], ssdOutput = [];
    let servNameId = [], servNumber = [];
    let value = "";
    for(let i = 0; i <= number; i++){  // push elements in array
        if(i > 0){
            value = i
        }
        coreOutput.push($('#coreOutput' + value).val());
        ramOutput.push($('#ramOutput' + value).val());
        sataOutput.push($('#sataOutput' + value).val());
        sasOutput.push($('#sasOutput' + value).val());
        ssdOutput.push($('#ssdOutput' + value).val());
        servNumber.push($('#servNumberId' + value).val());
        servNameId.push($('#servNameId' + value).val());
    }

    $.ajax({
        url: "http://127.0.0.1:5000/",
        method: "POST",
        data : {
            'core': coreOutput,
            'ram': ramOutput,
            'sata': sataOutput,
            'sas': sasOutput,
            'ssd': ssdOutput,
            'servNumber': servNumber,
            'servName': servNameId,
            'totalLength': number + 1,
            'clientName': $('#clientNameId').val(),
            'clientRequisites': $('#clientRequisitesId').val(),
        },
        success: function (res) { // принимает значение с Python и парсит его
            let value = ""
            res = $.parseJSON(res)
            result = res["result"]
            coreRes = res["coreRes"]
            ramRes = res["ramRes"]
            sataRes = res["sataRes"]
            sasRes = res["sasRes"]
            ssdRes = res["ssdRes"]
            for(let i = 0; i <= number; i++) {  // all results
                if (i > 0) {
                    value = i
                }
                $('#result' + value).text(result[i])
                $('#coreRes' + value).text(coreRes[i])
                $('#ramRes' + value).text(ramRes[i])
                $('#sataRes' + value).text(sataRes[i])
                $('#sasRes'+ value).text(sasRes[i])
                $('#ssdRes'+ value).text(ssdRes[i])
                $('#servNumerous' + value).text(i + 1)
            }
        },
        error: function () { // выводит ошибку, если значение не дошло до функции
            alert("Bad")
        }
    })
}


$(document).ready(function () { // когда документ готов к работе, то начинать проверку изменений

    $('#coreOutput').change(sendRequest);

    $('#ramOutput').change(sendRequest);

    $('#sataOutput').change(sendRequest);

    $('#sasOutput').change(sendRequest);

    $('#ssdOutput').change(sendRequest);

    $('#coreInput').change(sendRequest);

    $('#ramInput').change(sendRequest);

    $('#sataInput').change(sendRequest);

    $('#sasInput').change(sendRequest);

    $('#ssdInput').change(sendRequest);

    $('#servNumberId').change(sendRequest);

    $('#addServId').click(function (){
        addServ();
        $.ajax({
            url: "http://127.0.0.1:5000/",
            method: "POST",
            success: function (){
                let value = "";
                for(let i = 0; i <= number; i++) {  // all results
                    if (i > 0) {
                        value = i
                    }
                    $('#servNumerous' + value).text(i + 1)
                }
            }
        })

    });

})
