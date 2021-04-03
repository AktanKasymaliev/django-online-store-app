(function () {
    $( document ).ready(function () {
        var updateUser = '/user/upd/' + id + '/'
        var btn = $('.btn')
        btn.click(function(e) {
        e.preventDefault()
        var userName = $('#id_username')
        var mail = $('#id_email')
        var phone = $('#id_phone_number')
        var user = $('#user_ag')
        var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
//        var csrfmiddlewaretoken = $('input[name]').val()
            var data = {username: userName.val(), email: mail.val(), password: phone.val()}
            $.ajax({url: updateUser, type:"PATCH", data: data, headers:{"X-CSRFToken": $crf_token}, success: function(d) {
            alert('Your account updated successfully')
            }})
        })
    })
}) ()