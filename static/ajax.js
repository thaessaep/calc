const xhr = new XMLHttpRequest();

let number = 0

function addServ(){

    number += 1;

    let input = $('#duplicate').clone(true);

    let resInput = input.clone(true).find(':input, output').each(function(){ // clone part of html

        let newId = this.id + number;

        //client
        if(this.id == 'clientNameId'){
            $(this).attr({'id': newId, 'name': this.name+number});
        }
        else if(this.id == 'clientContractId'){
            $(this).attr({'id': newId, 'name': this.name+number});
        }
        else if(this.id == 'clientRequisitesId'){
            $(this).attr({'id': newId, 'name': this.name+number});
        }

        //serv
        else if(this.id == 'servNumberId'){
            $(this).attr({'id': newId, 'name': this.name+number});
        }
        else if(this.id == 'servNameId'){
            $(this).attr({'id': newId, 'name': this.name+number});
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
        else if(this.id == 'coreRes'){
            $(this).attr('id', newId);
        }
        else if(this.id == 'ramRes'){
            $(this).attr('id', newId);
        }
        else if(this.id == 'sataRes'){
            $(this).attr('id', newId);
        }
        else if(this.id == 'sasRes'){
            $(this).attr('id', newId);
        }
        else if(this.id == 'ssdRes'){
            $(this).attr('id', newId);
        }
        else if(this.id == 'result'){
            $(this).attr('id', newId);
        }

        console.log(this.id)

    }).end()

    $('#queue').append(resInput)

}


function sendRequest(){

    let coreOutput = [], ramOutput = [], sataOutput = [], sasOutput = [], ssdOutput = [], servNumber = [];

    for(let i = 0; i <= number; i++){  // push elements in array
        if(i == 0){
            coreOutput.push($('#coreOutput').val());
            ramOutput.push($('#ramOutput').val());
            sataOutput.push($('#sataOutput').val());
            sasOutput.push($('#sasOutput').val());
            ssdOutput.push($('#ssdOutput').val());
            servNumber.push($('#servNumberId').val());
        }
        else {
            coreOutput.push($('#coreOutput' + i).val());
            ramOutput.push($('#ramOutput' + i).val());
            sataOutput.push($('#sataOutput' + i).val());
            sasOutput.push($('#sasOutput' + i).val());
            ssdOutput.push($('#ssdOutput' + i).val());
            servNumber.push($('#servNumberId' + i).val());
        }
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
            'clientName': $('#clientNameId').val(),
            'clientContract': $('#clientContractId').val(),
            'clientRequisites': $('#clientRequisitesId').val(),
            'servName': $('#servNameId').val(),
        },
        success: function (res) { // принимает значение с Python и парсит его
            res = $.parseJSON(res)
            result = res["result"]
            coreRes = res["coreRes"]
            ramRes = res["ramRes"]
            sataRes = res["sataRes"]
            sasRes = res["sasRes"]
            ssdRes = res["ssdRes"]
            for(let i = 0; i <= number; i++) {  // all results
                if (i > 0) {
                    $('#result' + i).text(result[i])
                    $('#coreRes' + i).text(coreRes[i])
                    $('#ramRes' + i).text(ramRes[i])
                    $('#sataRes' + i).text(sataRes[i])
                    $('#sasRes'+ i).text(sasRes[i])
                    $('#ssdRes'+ i).text(ssdRes[i])
                }
                else {
                    $('#result').text(result[0])
                    $('#coreRes').text(coreRes[0])
                    $('#ramRes').text(ramRes[0])
                    $('#sataRes').text(sataRes[0])
                    $('#sasRes').text(sasRes[0])
                    $('#ssdRes').text(ssdRes[0])
                }
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

    $('#addServId').click(addServ);
})
