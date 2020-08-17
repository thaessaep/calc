$.ajax({
    url: 'superman',
    type: 'POST',
    data: jQuery.param({ field1: "hello", field2 : "hello2"}) ,
    contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
    success: function (response) {
        alert(response.status);
    },
    error: function () {
        alert("error");
    }
});