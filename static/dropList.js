
function dropList(){
    let objSel = document.getElementById('dropZip')
    $.ajax({
            url: "http://127.0.0.1:5000/view",
            method: "POST",
            data: {
                'value': 'dropList'
            },
            success: function (result){
                result = $.parseJSON(result)
                for (i = 0; i < result.length; i++) {
                    let option = document.createElement('option');
                    option.value = result[i];
                    objSel.append(option);
                }
                console.log(objSel)
            },
            error: function () {
                alert('Bad Request')
            }
        }
    )
}


$(document).ready(function () {
    dropList();

})