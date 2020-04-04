

function login() {
    var formdata = JSON.stringify($("#loginform").serializeArray(), undefined, 2);
        $.ajax({
            type: "POST",
            url: "/login/check",
            data: formdata,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                // var bgcontainer = $('#bgcontainer');
                // bgcontainer.html(response['bgcontainer']);
                // makebg();
                alert("logged in");
            },
            error: function (response) {
                alert('ERROR', response);
            }
        });
}
